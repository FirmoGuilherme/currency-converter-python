from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserRequest(BaseModel):
	id: Optional[int] = None
	name: str


class UserResponse(UserRequest):
	id: int
	created_at: datetime
	updated_at: Optional[datetime] = None

	class Config:
		orm_mode = True
		from_attributes=True