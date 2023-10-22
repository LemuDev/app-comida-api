from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(max_length=60)
    last_name: str = Field(max_length=60)
    email: str = Field(max_length=100)
    password: str = Field(max_length=255)
    
    is_admin: bool = Field(default=False)