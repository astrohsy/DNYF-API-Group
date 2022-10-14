# Third party imports
from pydantic import BaseModel


class GroupBaseDto(BaseModel):
    group_name: str
    accepting_new: bool


class GroupCreateDto(GroupBaseDto):
    pass


class GroupDto(GroupBaseDto):
    id: int

    class Config:
        orm_mode = True
