"""
Main API entrypoint
"""
# Third party imports
from fastapi import FastAPI

# Local application imports
from .routes import group

app = FastAPI()
app.include_router(group.router)
