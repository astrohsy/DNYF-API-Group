# Third party imports
from sqlalchemy.orm import Session

# Local application imports
from ..db.tables import Members
from ..schema.group import MemberPostDto


def create_member(db: Session, member: MemberPostDto) -> Members:
    db_member = Members(**member.dict())
    db.merge(db_member)
    db.commit()

    return db_member
