# Third party imports
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

# Local application imports
from .base import Base


class Association(Base):
    __tablename__ = "association_table"
    member_id = Column(ForeignKey("members.member_id"), primary_key=True)
    group_id = Column(ForeignKey("dnyf_groups.group_id"), primary_key=True)
    member = relationship("Members")



class Members(Base):
    __tablename__ = "members" 
    member_id = Column(Integer, primary_key=True)

