""" This is an example and should be replaced """
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


class GroupUserLink(SQLModel, table=True):
    group_id: int = Field(foreign_key='group.id', primary_key=True)
    user_id: int = Field(foreign_key='user.id', primary_key=True)

class UserBase(SQLModel):
    email: str
    password: str
    admin: bool
    groups: List["Group"] = Relationship(back_populates='users', link_model=GroupUserLink)


class UserCreate(UserBase):
    def into_db_model(self):
        model = User(
            email=self.email,
            password = self.password,
            admin = self.admin,
            groups = self.groups
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



class GroupBase(SQLModel):
    name: str = Field(max_length=64)
    description: Optional[str] = Field(default=None, max_length=256)
    users: List[User] = Relationship(back_populates='groups', link_model=GroupUserLink)


class Group(GroupBase, table=True):
    id: int = Field(default=None, primary_key=True)
    