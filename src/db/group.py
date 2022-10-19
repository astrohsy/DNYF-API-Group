# Third party imports
from sqlalchemy import Boolean, Column, Integer, String

# Local application imports
from .base import Base


class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    capacity = Column(Integer)
