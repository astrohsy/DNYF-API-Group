# Third party imports
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship

# Local application imports
from .base import Base
from .members import Members


class Group(Base):
    __tablename__ = "dnyf_groups"  # `groups` is a reserved word in MySQL...

    group_id = Column(Integer, primary_key=True)
    group_name = Column(String(100))
    group_capacity = Column(Integer)
    #members = relationship("Members",
    #                           secondary="member_id")
