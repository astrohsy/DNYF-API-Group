# Third party imports
from pydantic import BaseModel


class GroupBaseDto(BaseModel):
    group_name: str
    group_capacity: int
    

class GroupCreateDto(GroupBaseDto):
    group_capacity: int


class GroupDto(GroupBaseDto):
    group_id: int

    class Config:
        orm_mode = True
