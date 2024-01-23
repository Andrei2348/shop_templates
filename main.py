from fastapi import FastAPI, Request
import sqlalchemy
from pydantic import BaseModel, Field
from typing import List
from models import *
from valid import *


app = FastAPI()

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)


# Users
@app.get("/users/", response_model=List[Users])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get("/users/{user_id}", response_model=Users)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.post("/users/", response_model=Users)
async def create_user(user: UsersIn):
    query = users.insert().values(**user.model_dump())
    record_id = await database.execute(query)
    return{**user.model_dump(), "id": record_id}


@app.put("/users/{user_id}", response_model=Users)
async def update_user(user_id: int, new_user: UsersIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}


# Products
@app.get("/products/", response_model=List[Products])
async def read_products():
    query = products.select()
    return await database.fetch_all(query)


@app.get("/products/{product_id}", response_model=Products)
async def read_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    return await database.fetch_one(query)


@app.post("/products/", response_model=Products)
async def create_product(product: ProductsIn):
    query = products.insert().values(**product.model_dump())
    record_id = await database.execute(query)
    return{**product.model_dump(), "id": record_id}


@app.put("/products/{product_id}", response_model=Products)
async def update_product(product_id: int, new_product: ProductsIn):
    query = products.update().where(products.c.id == product_id).values(**new_product.dict())
    await database.execute(query)
    return {**new_product.dict(), "id": product_id}


@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    return {'message': 'Product deleted'}


# Orders
@app.get("/orders/", response_model=List[Orders])
async def read_orders():
    query = orders.select()
    return await database.fetch_all(query)


@app.get("/orders/{order_id}", response_model=Orders)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)


@app.post("/orders/", response_model=Orders)
async def create_order(order: OrdersIn):
    query = orders.insert().values(**order.model_dump())
    record_id = await database.execute(query)
    return{**order.model_dump(), "id": record_id}


@app.put("/orders/{order_id}", response_model=Orders)
async def update_order(order_id: int, new_order: OrdersIn):
    query = orders.update().where(orders.c.id == order_id).values(**new_order.dict())
    await database.execute(query)
    return {**new_order.dict(), "id": order_id}


@app.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {'message': 'Order deleted'}