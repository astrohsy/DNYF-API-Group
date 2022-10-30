# Third party imports
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

# Local application imports
from .base import Base


association_table = Table(
    "association_table",
    Base.metadata,
    Column(
        "member_id",
        Integer,
        ForeignKey("members.member_id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column(
        "group_id",
        Integer,
        ForeignKey("dnyf_groups.group_id", ondelete="CASCADE"),
        nullable=False,
    ),
)


class Members(Base):
    __tablename__ = "members"
    member_id = Column(Integer, primary_key=True)
    groups = relationship(
        "Group",
        secondary=association_table,
        back_populates="members",
        passive_deletes=True,
    )


class Group(Base):
    __tablename__ = "dnyf_groups"  # `groups` is a reserved word in MySQL...
    group_id = Column(Integer, primary_key=True)
    group_name = Column(String(100))
    group_capacity = Column(Integer)
    members = relationship(
        "Members",
        secondary=association_table,
        back_populates="groups",
        cascade="all, delete",
    )
