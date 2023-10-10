from sqlmodel import SQLModel, Field
from typing import Optional

class Restaurant(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    user_id: Optional[int] = Field(default=None, foreign_key='user.id')