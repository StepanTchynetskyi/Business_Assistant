from pydantic import BaseModel
from uuid import UUID
from app.api.user import schemas as user_schemas


class CreateUser(BaseModel):
    email: str
    password: str
    name: str
    last_name: str


class CreatedUser(BaseModel):
    id: UUID
    email: str


class LoginForm(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
