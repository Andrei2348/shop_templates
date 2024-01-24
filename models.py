import sqlalchemy
import databases
from datetime import datetime


DATABASE_URL = "sqlite:///mydatabase.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("firstname", sqlalchemy.String(40)),
    sqlalchemy.Column("lastname", sqlalchemy.String(40)),
    sqlalchemy.Column("email", sqlalchemy.String(40)),
    sqlalchemy.Column("password", sqlalchemy.String(40)),
)


products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("price", sqlalchemy.Float(20)),
    sqlalchemy.Column("title", sqlalchemy.String(20)),
    sqlalchemy.Column("description", sqlalchemy.String(200)),
)


orders = sqlalchemy.Table(
    "orders",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("date", sqlalchemy.DateTime(), default=datetime.now()),
    sqlalchemy.Column("status", sqlalchemy.Boolean, default=True),
    sqlalchemy.Column("users_id", sqlalchemy.ForeignKey("users.id")),
    sqlalchemy.Column("products_id", sqlalchemy.ForeignKey("products.id")),
)
