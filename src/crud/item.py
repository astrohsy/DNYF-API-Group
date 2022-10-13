from sqlalchemy.orm import Session

from ..db.item import Item


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()
