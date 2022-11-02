"""
User endpoint routing
"""
# Standard library imports
from typing import List

# Third party imports
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# Local application imports
from ..db.base import get_db
from ..schema.group import GroupDto, GroupCreateDto, MemberDto, GroupDtoPaginated
from ..crud import group as group_crud

router = APIRouter(prefix="/groups", tags=["groups"])

DEFAULT_OFFSET = 0
DEFAULT_LIMIT = 100


@router.get("/", response_model=GroupDtoPaginated)
def read_groups(
    offset: int = DEFAULT_OFFSET,
    limit: int = DEFAULT_LIMIT,
    db: Session = Depends(get_db),
):
    groups = group_crud.get_groups(db, offset=offset, limit=limit)

    total = group_crud.count_groups(db)
    links = []

    if offset + limit < total:
        links.append(
            {
                "href": f"/groups?offset={offset + limit}&limit={limit}",
                "rel": "get_next_group_page",
                "type": "GET",
            }
        )

    if offset > 0:
        prev = max(0, offset - limit)
        links.append(
            {
                "href": f"/groups?offset={prev}&limit={limit}",
                "rel": "get_prev_group_page",
                "type": "GET",
            }
        )

    return GroupDtoPaginated(data=groups, links=links)


@router.get("/{group_id}", response_model=GroupDto)
def read_group(group_id: int, db: Session = Depends(get_db)):
    db_group = group_crud.get_group(db, group_id=group_id)

    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")

    return db_group


@router.get("/{group_id}/members", response_model=List[MemberDto])
def get_members(
    group_id: int,
    db: Session = Depends(get_db),
):
    members = group_crud.get_members(group_id=group_id, db=db)
    return members


@router.post("/", response_model=GroupDto)
def create_group(group: GroupCreateDto, db: Session = Depends(get_db)):
    return group_crud.create_group(db=db, group=group)


@router.post("/{group_id}/members", response_model=GroupDto)
def add_member(new_member: dict, group_id: int, db: Session = Depends(get_db)):
    db_group = group_crud.get_group(db, group_id=group_id)
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")

    return group_crud.add_member(db=db, new_member=new_member, group_id=group_id)


@router.delete("/{group_id}", response_model=GroupDto)
def delete_group(group_id: int, db: Session = Depends(get_db)):
    # Raise an error here
    db_group = group_crud.get_group(db, group_id=group_id)
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")

    return group_crud.delete_group(db=db, group_id=group_id)


@router.delete("/{group_id}/members/{member_id}", response_model=GroupDto)
def delete_member(group_id: int, member_id: int, db: Session = Depends(get_db)):
    # Raise an error here
    return group_crud.delete_member(db=db, group_id=group_id, member_id=member_id)


@router.put("/{group_id}", response_model=GroupDto)
def put_groupname(new_group: dict, group_id: int, db: Session = Depends(get_db)):
    # Raise an error here
    return group_crud.put_groupname(new_group=new_group, db=db, group_id=group_id)
