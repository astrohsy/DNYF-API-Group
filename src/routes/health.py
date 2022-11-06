# Standard library imports
from datetime import datetime

# Third party imports
from fastapi import APIRouter


router = APIRouter()


@router.get("/health", tags=["health"])
async def get_health():
    t = str(datetime.now())
    msg = {"name": "Groups Api", "health": "Good", "at time": t}

    return msg
