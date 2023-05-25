import email
from fastapi import Body
from pydantic import BaseModel
from passlib.context import CryptContext
from typing import List

from pydantic import BaseModel


class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    title: str
    body: str

    class Config():
        orm_mode = True


class User(BaseModel):
    username: str
    email: str
    password: str


class ShowUser(BaseModel):
    username: str
    email: str
    blogs: List[Blog]

    class Config():
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str
    author: ShowUser

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
