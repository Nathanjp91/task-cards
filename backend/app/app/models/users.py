""" This is an example and should be replaced """
from sqlmodel import SQLModel, Field
from typing import Optional

class UserBase(SQLModel):
    email: str
    password: str
    admin: bool


class UserCreate(UserBase):
    pass

    def into_db_model(self):
        model = User(
            email=self.email,
            password = self.password,
            admin = self.admin
        )
        return model


class UserUpdate(SQLModel):
    email: Optional[str] = None
    password: Optional[str] = None
    admin: Optional[bool] = None
    

class User(UserBase, table=True):
    id: int = Field(default=None, primary_key=True)

    def update(self, user: UserCreate):
        for key, value in user.__dict__.items():
            setattr(self, key, value)

