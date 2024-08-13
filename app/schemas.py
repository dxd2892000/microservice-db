from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# User Schemas
class UserBase(BaseModel):
    name: str
    password: str
    createdTime: Optional[datetime] = None

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    inferences: List['Inference'] = []

    class Config:
        from_attributes = True

# Inference Schemas
class InferenceBase(BaseModel):
    name: str
    url: str
    result: str
    createdTime: Optional[datetime] = None

class InferenceCreate(InferenceBase):
    pass

class Inference(InferenceBase):
    id: int
    user_id: Optional[int] = None
    user: Optional[User] = None

    class Config:
        from_attributes = True

