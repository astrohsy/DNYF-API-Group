# Local application imports
from .schema.group import GroupPostDto, MemberPostDto
from .db.base import SessionLocal
from .crud import group as group_crud
from .crud import member as member_crud


sample_groups = [
    {"group_name": "OS Study Group", "group_capacity": 4},
    {"group_name": "Learning Java", "group_capacity": 2},
    {"group_name": "Algo Midterm", "group_capacity": 3},
    {"group_name": "DB Project", "group_capacity": 4},
    {"group_name": "6156 Project", "group_capacity": 5},
    {"group_name": "PLT Peer Programming", "group_capacity": 2},
]

sample_members = [
    {"member_id": 1},
    {"member_id": 2},
    {"member_id": 3},
    {"member_id": 4},
    {"member_id": 5},
    {"member_id": 6},
]


sample_group_memberships = [
    (1, {"member_id": 1}),
    (1, {"member_id": 2}),
    (1, {"member_id": 3}),
    (2, {"member_id": 4}),
    (2, {"member_id": 5}),
    (3, {"member_id": 6}),
]


def add_sample_data():
    db = SessionLocal()

    for group in sample_groups:
        group_crud.create_group(db=db, group=GroupPostDto(**group))

    for member in sample_members:
        member_crud.create_member(db=db, member=MemberPostDto(**member))

    for group_id, member in sample_group_memberships:
        group_crud.add_member_to_group(
            db=db, group_id=group_id, new_member=MemberPostDto(**member)
        )

    db.close()
