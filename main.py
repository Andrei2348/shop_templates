from fastapi import FastAPI, Request
import sqlalchemy
import databases
from pydantic import BaseModel, Field
from typing import List


DATABASE_URL = "sqlite:///mydatabase.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.Metadata()

app = FastAPI()


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
    price: str = Field(max_length=20)
    title: str = Field(max_length=20)
    description: str = Field(max_length=200)


class ProductsIn(BaseModel):
    price: str = Field(max_length=20)
    title: str = Field(max_length=20)
    description: str = Field(max_length=200)


engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)


@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(**user.model_dump())
    record_id = await database.execute(query)
    return{**user.model_dump(), "id": record_id}


@app.get("/users/", response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id ==user_id).values(**new_user)
    await database.execute(query)
    return {**new_user, "id": user_id}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}