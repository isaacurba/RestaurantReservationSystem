from pydantic import BaseModel, Field, EmailStr
from src.models.user_role import UserRole


class UserCreate(BaseModel):
    full_name: str = Field(min_length=1, max_length=50)
    email: EmailStr
    password: str = Field(min_length=1, max_length=200)
    role: UserRole = UserRole.CUSTOMER
    is_active: bool = False


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class CustomerCreate(BaseModel):
    address: str = Field(min_length=1, max_length=200)

class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    role: UserRole
    is_active: bool

    class Config:
        from_attributes = True