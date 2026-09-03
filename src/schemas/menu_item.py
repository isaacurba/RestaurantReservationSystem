from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

from src.models.category import Category


class MenuItemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: Decimal
    category: Category
    description: str = Field(min_length=1, max_length=255)
    menu_id: int


class MenuItemUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    price: Decimal | None = None
    category: Category | None = None
    description: str | None = Field(default=None, min_length=1, max_length=255)


class MenuItemResponse(BaseModel):
    id: int
    menu_id: int
    name: str
    price: Decimal
    category: Category
    description: str

    model_config = ConfigDict(from_attributes=True)