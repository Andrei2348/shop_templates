from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    firstname: str = Field(max_length=40)
    lastname: str = Field(max_length=40)
    email: str = Field(max_length=40)
    password: str = Field(max_length=40)
    orders: int = Field(max_length=4)


class UserIn(BaseModel):
    firstname: str = Field(max_length=40)
    lastname: str = Field(max_length=40)
    email: str = Field(max_length=40)
    password: str = Field(max_length=40)
    orders: int = Field(max_length=4)  


class Products(BaseModel):
    id: int
    price: float = Field(max_length=20)
    title: str = Field(max_length=20)
    description: str = Field(max_length=200)


class ProductsIn(BaseModel):
    price: float = Field(max_length=20)
    title: str = Field(max_length=20)
    description: str = Field(max_length=200)


class Orders(BaseModel):
    id: int
    date: str = Field(max_length=20)
    status: bool = Field(max_length=10)
    users_id: int = Field(max_length=10)
    products_id: int = Field(max_length=10)


class OrdersIn(BaseModel):
    date: str = Field(max_length=20)
    status: bool = Field(max_length=10)
    users_id: int = Field(max_length=10)
    products_id: int = Field(max_length=10)
