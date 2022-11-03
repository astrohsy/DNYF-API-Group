# Standard library imports
from enum import Enum

# Third party imports
from pydantic import BaseModel, validator
from typing import List, Optional, Union


class HTTPMethod(str, Enum):
    get = "GET"
    post = "POST"
    put = "PUT"
    delete = "DELETE"


class Link(BaseModel):
    """Link properties."""

    href: str
    rel: str
    type: HTTPMethod


class GroupBaseDto(BaseModel):
    """Shared properties."""

    group_name: str
    group_capacity: int


class GroupPostDto(GroupBaseDto):
    """Group properties to receive on group creation."""

    pass


class GroupPutDto(GroupBaseDto):
    """Group properties to receive on group update."""

    group_name: Union[str, None] = None
    group_capacity: Union[int, None] = None


class GroupDto(GroupBaseDto):
    """Group roperties with links."""

    group_id: int
    links: Optional[List[Link]]

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


class GroupGetDto(BaseModel):
    """Group properties to return to client."""

    data: GroupDto

    class Config:
        orm_mode = True


class GroupGetDtoPaginated(BaseModel):
    """Group roperties to return to client with pagination."""

    data: List[GroupDto]
    links: List[Link]

    class Config:
        orm_mode = True


class MemberDto(BaseModel):
    member_id: int
    links: List[Link]

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


class MemberPostDto(BaseModel):
    """Member properties to receive on member creation."""

    member_id: int


class MemberGetDto(BaseModel):
    """Member properties to return to client."""

    data: List[MemberDto]

    class Config:
        orm_mode = True
