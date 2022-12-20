from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel


class Message(BaseModel):
    id: Optional[UUID] = uuid4()
    pfp: Optional[str] = ""
    username: str
    message: str


class EditMessage(BaseModel):
    id: UUID
    message: str
