# Standard library imports
from typing import List, Union

# Third party imports
from sqlalchemy.orm import Session

# Local application imports
from ..db.group import Group
from ..db.members import Members, Association
from ..schema.group import GroupCreateDto, GroupBaseDto

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

def delete_group(db: Session, group_id: int) -> Union[Group, None]: 
    db_group = db.query(Group).filter(Group.group_id == group_id).first()
    deleted_group = db_group
    db.delete(db_group)
    db.commit()
    db.refresh
    return deleted_group

def put_groupname(new_group: dict, db: Session,  group_id: int) -> Union[Group, None]: 
    db.query(Group).filter(Group.group_id == group_id).update(new_group, synchronize_session="fetch")
    db.commit()
    db.refresh
    db_group = db.query(Group).filter(Group.group_id == group_id).first()
    return db_group

def add_member(new_member: dict, db: Session,  group_id: int) -> Union[Group, None]: 
    #db.query(Group).filter(Group.group_id == group_id).update(new_group, synchronize_session="fetch")
    assoc = Association(**new_member)
    db.add(assoc)
    db.commit()
    db.refresh
    db_group = db.query(Group).filter(Group.group_id == group_id).first()
    return db_group
