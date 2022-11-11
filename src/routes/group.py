"""
Group endpoint routing
"""
# Third party imports
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# Local application imports
from ..db.base import get_db
from ..schema.group import (
    GroupGetDto,
    GroupPostDto,
    GroupPutDto,
    GroupGetDtoPaginated,
    MemberGetDto,
    MemberPostDto,
)
from ..crud import group as group_crud


router = APIRouter(prefix="/groups", tags=["groups"])

DEFAULT_OFFSET = 0
DEFAULT_LIMIT = 100


@router.get("/", response_model=GroupGetDtoPaginated)
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

    return GroupGetDtoPaginated(data=groups, links=links)


@router.get("/{group_id}", response_model=GroupGetDto)
def read_group(group_id: int, db: Session = Depends(get_db)):
    db_group = group_crud.get_group(db, group_id=group_id)

    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")

    return GroupGetDto(data=db_group)


@router.get("/{group_id}/members", response_model=MemberGetDto)
def get_members(
    group_id: int,
    db: Session = Depends(get_db),
):
    members = group_crud.get_members(group_id=group_id, db=db)
    return MemberGetDto(data=members)


@router.post("/", response_model=GroupGetDto)
def create_group(group: GroupPostDto, db: Session = Depends(get_db)):
    db_group = group_crud.create_group(db=db, group=group)
    return GroupGetDto(data=db_group)


@router.post("/{group_id}/members", response_model=GroupGetDto)
def add_member_to_group(
    new_member: MemberPostDto, group_id: int, db: Session = Depends(get_db)
):
    db_group = group_crud.get_group(db, group_id=group_id)
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")

    db_group = group_crud.add_member_to_group(
        db=db, new_member=new_member, group_id=group_id
    )
    return GroupGetDto(data=db_group)


@router.delete("/{group_id}", response_model=GroupGetDto)
def delete_group(group_id: int, db: Session = Depends(get_db)):
    # Raise an error here
    db_group = group_crud.get_group(db, group_id=group_id)
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")

    db_group = group_crud.delete_group(db=db, group_id=group_id)
    return GroupGetDto(data=db_group)


@router.delete("/{group_id}/members/{member_id}", response_model=GroupGetDto)
def delete_member(group_id: int, member_id: int, db: Session = Depends(get_db)):
    # Raise an error here
    db_group = group_crud.delete_member(db=db, group_id=group_id, member_id=member_id)
    return GroupGetDto(data=db_group)


@router.put("/{group_id}", response_model=GroupGetDto)
def edit_group(new_group: GroupPutDto, group_id: int, db: Session = Depends(get_db)):
    # Raise an error here
    db_group = group_crud.edit_group(new_group=new_group, db=db, group_id=group_id)
    return GroupGetDto(data=db_group)
