# Third party imports
from sqlalchemy import Column, Integer, String

# Local application imports
from .base import Base


class Group(Base):
    __tablename__ = "dnyf_groups"  # `groups` is a reserved word in MySQL...

    group_id = Column(Integer, primary_key=True)
    group_name = Column(String(100))
