# Third party imports
from pydantic import BaseModel, validator
from typing import List, Dict, Optional


class GroupBaseDto(BaseModel):
    group_name: str
    group_capacity: int


class GroupCreateDto(GroupBaseDto):
    pass


class GroupDto(GroupBaseDto):
    group_id: int
    links: Optional[List[Dict]]

    @validator("links", always=True)
    def validate_links(cls, value, values):
        links = [
            {"href": f'/groups/{values["group_id"]}', "rel": "self", "type": "GET"},
            {
                "href": f'/groups/{values["group_id"]}/members',
                "rel": "get_members",
                "type": "GET",
            },
            {
                "href": f'/groups/{values["group_id"]}',
                "rel": "delete_group",
                "type": "DELETE",
            },
            {
                "href": f'/groups/{values["group_id"]}',
                "rel": "edit_group",
                "type": "PUT",
            },
        ]
        return links

    class Config:
        orm_mode = True


class MemberDto(BaseModel):
    member_id: int
    links: Optional[List[Dict]]

    @validator("links", always=True)
    def validate_links(cls, value, values):
        links = [
            {
                "href": f'/users/{values["member_id"]}',
                "rel": "get_user_info",
                "type": "GET",
            }
        ]
        return links

    class Config:
        orm_mode = True
