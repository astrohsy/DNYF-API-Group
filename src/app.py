"""
Main API entrypoint
"""
# Third party imports
from fastapi import FastAPI

# Local application imports
from .routes import group
from .routes import health
from .db.base import engine, Base

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(group.router)
app.include_router(health.router)
