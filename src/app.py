"""
Main API entrypoint
"""
# Third party imports
from fastapi import FastAPI

# Local application imports
from .routes import group, health

app = FastAPI()
app.include_router(group.router)
app.include_router(health.router)
