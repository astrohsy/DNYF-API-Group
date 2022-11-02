# Local application imports
from .schema.group import GroupPostDto
from .db.base import SessionLocal
from .crud import group as group_crud


sample_groups = [
    {"group_name": "OS Study Group", "group_capacity": 4},
    {"group_name": "Learning Java", "group_capacity": 2},
    {"group_name": "Algo Midterm", "group_capacity": 3},
    {"group_name": "DB Project", "group_capacity": 4},
    {"group_name": "6156 Project", "group_capacity": 5},
    {"group_name": "PLT Peer Programming", "group_capacity": 2},
]


def add_sample_data():
    db = SessionLocal()
    for group in sample_groups:
        group_crud.create_group(db=db, group=GroupPostDto(**group))
    db.close()
