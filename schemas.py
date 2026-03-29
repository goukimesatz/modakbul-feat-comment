from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional

# --- USER SCHEMAS ---
class UserCreate(BaseModel):
    username: str = Field(..., max_length=127)
    password: str

class UserResponse(BaseModel):
    id: UUID
    username: str

    class Config:
        from_attributes = True

# --- TOPIC SCHEMAS ---
class TopicCreate(BaseModel):
    content: str = Field(..., max_length=127)

class TopicResponse(BaseModel):
    id: UUID
    owner_id: UUID
    content: str
    topic_hash: str
    ttl: datetime
    current_comment_number: int = 0
    previous_comment_number: int = 0
    total_comment_number: int = 0

    class Config:
        from_attributes = True

# --- COMMENT SCHEMAS ---
class CommentCreate(BaseModel):
    content: str = Field(..., max_length=1023)

class CommentResponse(BaseModel):
    id: UUID
    owner_id: UUID
    topic_id: UUID
    content: str

    class Config:
        from_attributes = True
