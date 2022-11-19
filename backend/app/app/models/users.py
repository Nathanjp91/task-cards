""" This is an example and should be replaced """
from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    email: str
    password: str
    admin: bool


class UserCreate(UserBase):
    pass


class User(UserBase, table=True):
    id: int = Field(default=None, primary_key=True)

    def update(self, user: UserCreate):
        for key, value in user.__dict__.items():
            setattr(self, key, value)

