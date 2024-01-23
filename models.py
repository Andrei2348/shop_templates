import sqlalchemy

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("firstname", sqlalchemy.String(40)),
    sqlalchemy.Column("lastname", sqlalchemy.String(40)),
    sqlalchemy.Column("email", sqlalchemy.String(40)),
    sqlalchemy.Column("password", sqlalchemy.String(40)),
    # orders = relationship("orders", back_populates="users"),
)


products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("price", sqlalchemy.Float(20)),
    sqlalchemy.Column("title", sqlalchemy.String(20)),
    sqlalchemy.Column("description", sqlalchemy.String(200)),
    # orders = relationship("orders", back_populates="products"),
)


orders = sqlalchemy.Table(
    "orders",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("date", sqlalchemy.DateTime()),
    sqlalchemy.Column("status", sqlalchemy.Boolean, default=True),
    sqlalchemy.Column("users_id", sqlalchemy.ForeignKey("users.id")),
    sqlalchemy.Column("products_id", sqlalchemy.ForeignKey("products.id")),
    # users = relationship("users", back_populates="orders"),
    # products = relationship("products", back_populates="orders")
)
