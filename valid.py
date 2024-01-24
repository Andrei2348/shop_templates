from pydantic import BaseModel, Field
from datetime import datetime


class Users(BaseModel):
    id: int
    firstname: str = Field(max_length=40)
    lastname: str = Field(max_length=40)
    email: str = Field(max_length=40)
    password: str = Field(max_length=40)
   

class UsersIn(BaseModel):
    firstname: str = Field(max_length=40)
    lastname: str = Field(max_length=40)
    email: str = Field(max_length=40)
    password: str = Field(max_length=40)


class Products(BaseModel):
    id: int
    price: float = Field()
    title: str = Field(max_length=20)
    description: str = Field(max_length=200)


class ProductsIn(BaseModel):
    price: float = Field()
    title: str = Field(max_length=20)
    description: str = Field(max_length=200)


class Orders(BaseModel):
    id: int
    date: datetime = None
    status: bool
    users_id: int = Field()
    products_id: int = Field()

    
class OrdersIn(BaseModel):
    status: bool
    users_id: int = Field()
    products_id: int = Field()
