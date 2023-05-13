from sqlalchemy import (
    Table, 
    MetaData, 
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
)

meta_obj = MetaData()

users_table = Table(
    "user",
    meta_obj,
    Column("id",Integer, primary_key=True),
    Column("username", String(20), unique=True, nullable=False),
    Column("firstName",String(30), nullable=False),
    Column("lastName",String(30), nullable=False)
)


posts_table = Table(
    "posts",
    meta_obj,
    Column("id", Integer, primary_key=True),
    Column("title", String(255), nullable=False),
    Column("content", Text()),
    Column("user",ForeignKey("user.id"))
)
