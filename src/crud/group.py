# Standard library imports
from typing import List, Union

# Third party imports
from sqlalchemy.orm import Session

# Local application imports
from ..db.tables import Members, association_table, Group
from ..schema.group import GroupPostDto, GroupPutDto, MemberPostDto


def get_group(db: Session, group_id: int) -> Union[Group, None]:
    return db.query(Group).filter(Group.group_id == group_id).first()


def count_groups(db: Session) -> int:
    return db.query(Group).count()


def get_groups(db: Session, offset: int = 0, limit: int = 10) -> List[Group]:
    return db.query(Group).offset(offset).limit(limit).all()


def get_members(group_id: int, db: Session) -> List[Members]:
    assoc = (
        db.query(association_table)
        .filter(association_table.c.group_id == group_id)
        .all()
    )

    return assoc


def create_group(db: Session, group: GroupPostDto) -> Group:
    db_group = Group(**group.dict())
    db.add(db_group)
    db.commit()
    db.refresh(db_group)

    return db_group


def delete_group(db: Session, group_id: int) -> Union[Group, None]:
    db_group = db.query(Group).filter(Group.group_id == group_id).first()
    deleted_group = db_group
    db.delete(db_group)
    db.commit()

    return deleted_group


def edit_group(
    new_group: GroupPutDto, db: Session, group_id: int
) -> Union[Group, None]:
    db.query(Group).filter(Group.group_id == group_id).update(
        new_group.dict(exclude_none=True), synchronize_session="fetch"
    )
    db.commit()
    db_group = db.query(Group).filter(Group.group_id == group_id).first()

    return db_group


def add_member_to_group(
    new_member: MemberPostDto, db: Session, group_id: int
) -> Union[Group, None]:
    """
    TODO: This currently doesn't work
    """
    db.execute(
        association_table.insert(),
        params=new_member,
    )
    db.commit()
    db_group = db.query(Group).filter(Group.group_id == group_id).first()

    return db_group


def delete_member(db: Session, group_id: int, member_id: int) -> Union[Group, None]:
    db.query(association_table).filter(
        association_table.c.group_id == group_id,
        association_table.c.member_id == member_id,
    ).delete()
    db.commit()
    db_group = db.query(Group).filter(Group.group_id == group_id).first()

    return db_group
