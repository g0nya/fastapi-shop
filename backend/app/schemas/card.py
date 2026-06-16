from token import OP

from attr import field
from pydantic import BaseModel, Field
from typing import Optional


class CartItemBase(BaseModel):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="Quantity of product")


class CartItemCreate(CartItemBase):
    pass


class CartItemUpdate(BaseModel):
    product_id: int = Field(..., description="Product id")
    quantity: int = Field(..., gt=0, description="Quantity of product")


class CartItem(BaseModel):
    product_id: int
    name: str = Field(..., description="Product name")
    price: float = Field(..., description="Product price")
    quantity: int = Field(..., description="Quantity product")
    subtotal: int = Field(..., description="Total price for this item(price*quantity)")
    image_url: Optional[str] = Field(None, description="Product image url")


class CartResponse(BaseModel):
    items: list[CartResponse] = Field(..., description="list of items")
    total: float = Field(..., description="total price")
    items_count: int = Field(..., description="Total number of items in card")
