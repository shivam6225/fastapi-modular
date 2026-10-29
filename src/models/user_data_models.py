from typing import List, Optional

from pydantic import BaseModel, Field

#Pydantic model allows for data validation and serialization. 
#It is used to define the structure of the data that will be sent and received by the API endpoints.

#Model for Get User Data Request
class GetUserDataRequest(BaseModel):
    user_id: int = Field(..., description="The ID of the user to retrieve data for")

#Field(...) indicates that the user_id field is required and must be provided in the request.

class UserData(BaseModel):
    user_id: int = Field(..., description="The ID of the user")
    name: str = Field(..., description="The name of the user")
    email: str = Field(..., description="The email address of the user")
    age: Optional[int] = Field(None, description="The age of the user (optional)")
    address: Optional[str] = Field(None, description="The address of the user (optional)")

#Optional fields (age and address) are defined with Optional type hints, 
#In this case, they can be omitted from the response if not applicable or empty.