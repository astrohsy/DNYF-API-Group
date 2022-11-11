"""
Main API entrypoint
"""
# Standard library imports
import json

# Third party imports
from fastapi import FastAPI, Request
from starlette.responses import StreamingResponse
from starlette.concurrency import iterate_in_threadpool
import boto3

# Local application imports
from .routes import group
from .routes import health
from .routes import base
from .db.base import engine, Base
from .sample_data import add_sample_data
from src.config import settings

# Create all DB schema from scratch on every startup
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

# Add sample data to DB
add_sample_data()

app = FastAPI()
base.router.include_router(group.router)
base.router.include_router(health.router)
app.include_router(base.router)


# Add SNS middleware
sns_resource = boto3.resource(
    "sns",
    region_name="us-east-1",
    aws_access_key_id=settings.aws_access_key,
    aws_secret_access_key=settings.aws_secret,
)
sns_topic = sns_resource.Topic(settings.sns_topic_arn)


@app.middleware("http")
async def sns_middleware(request: Request, call_next):
    response: StreamingResponse = await call_next(request)

    if request.method == "POST" and request.url.path == "/api/groups/":
        # Get response body
        # https://stackoverflow.com/questions/71882419/fastapi-how-to-get-the-response-body-in-middleware
        response_body_raw = [chunk async for chunk in response.body_iterator]
        response.body_iterator = iterate_in_threadpool(iter(response_body_raw))
        response_body = json.loads((b"".join(response_body_raw)).decode())

        # Publish to SNS
        message = (
            f"Created group \"{response_body['data']['group_name']}\" "
            f"with capacity {response_body['data']['group_capacity']}"
        )
        sns_topic.publish(Message=message)

    return response
