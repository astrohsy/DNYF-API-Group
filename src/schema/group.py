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

    links: Optional[List[Dict]]
    @validator("links", always=True)
    def validate_links(cls, value, values):
        l = [
        {
            "href": f'/groups/{values["group_id"]}',
            "rel": "self",
            "type" : "GET"
        },
        {
            "href": f'/groups/{values["group_id"]}/members',
            "rel": "get_members",
            "type" : "GET"
        },
        {
            "href": f'/groups/{values["group_id"]}',
            "rel": "delete_group",
            "type" : "DELETE"
        },
        {
            "href": f'/groups/{values["group_id"]}',
            "rel": "edit_group",
            "type" : "PUT"
        }
     ]
        return l 
    
    class Config:
        orm_mode = True

class MemberDto(BaseModel):
    member_id: int
    links: Optional[List[Dict]]
        
    @validator("links", always=True)
    def validate_links(cls, value, values):
        l = [{
            "href": f'/users/{values["member_id"]}',  
            "rel": "get_user_info",
            "type" : "GET"
        }
        ]
        return l
    #group_id:int

    class Config:
        orm_mode = True


#member links
#  "links": [
#         {
# // get user info from users microservice
#             "href": "/users/{id}",  
#             "rel": "get_user_info",
#             "type" : "GET"
#         },
#         {
# // remove user from group
#             "href": "/groups/123/members/456",  
#             "rel": "delete_from_group",
#             "type" : "DELETE"
#         }
# group links 
#   "links": [
#         {
#             "href": "/groups/{id}",
#             "rel": "self",
#             "type" : "GET"
#         },
#         {
#             "href": "/groups/{id}/members",
#             "rel": "get_members",
#             "type" : "GET"
#         },
#         {
#             "href": "/groups/{id}",
#             "rel": "delete_group",
#             "type" : "DELETE"
#         },
#   {
#             "href": "/groups/{id}",
#             "rel": "edit_group",
#             "type" : "PUT"
#         }
#      ]
