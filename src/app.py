"""
Main API entrypoint
"""
# Third party imports
from fastapi import FastAPI

# Local application imports
from .routes import item, user

app = FastAPI()
app.include_router(user.router)
app.include_router(item.router)
