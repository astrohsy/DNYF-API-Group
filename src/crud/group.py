# Standard library imports
from typing import List, Union

# Third party imports
from sqlalchemy.orm import Session

# Local application imports
from ..db.group import Group
from ..schema.group import GroupCreateDto


def get_group(db: Session, group_id: int) -> Union[Group, None]:
    return db.query(Group).filter(Group.group_id == group_id).first()


def get_groups(db: Session, offset: int = 0, limit: int = 10) -> List[Group]:
    return db.query(Group).offset(offset).limit(limit).all()


def create_group(db: Session, group: GroupCreateDto) -> Group:
    db_group = Group(**group.dict())
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group
