# Standard library imports
from typing import List
from datetime import datetime

# Third party imports
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# Local application imports
from ..db.base import get_db
from ..schema.group import GroupDto, GroupCreateDto
from ..crud import group as group_crud


router = APIRouter()

@router.get("/")
async def get_whatever():
    return "hello"

@router.get("/api/health")
async def get_health():
    t = str(datetime.now())
    msg = {
        "name": "Groups Api",
        "health": "Good",
        "at time": t
    }
    return msg 