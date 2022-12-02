""" This is an example and should be replaced """
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


class TaskTagLink(SQLModel, table=True):
    task_id: int = Field(foreign_key='task.id', primary_key=True)
    tag_id: int = Field(foreign_key='tag.id', primary_key=True)


class TaskBase(SQLModel):
    name: str = Field(max_length=64)
    text: str = Field(max_length=1024)
    image_url: Optional[str] = Field(default=None, max_length=256)
    value: Optional[int] = Field(default=None)
    tags: List["tag"] = Relationship(back_populates='task', link_model=TaskTagLink)
    


class TaskCreate(TaskBase):
    pass


class TaskUpdate(SQLModel):
    name: Optional[str] = Field(default=None, max_length=64)
    text: Optional[str] = Field(default=None, max_length=1024)
    image_url: Optional[str] = Field(default=None, max_length=256)
    value: Optional[int] = Field(default=None)

class Task(TaskBase, table=True):
    id: int = Field(default=None, primary_key=True)

    def update(self, task: TaskCreate):
        for key, value in task.__dict__.items():
            setattr(self, key, value)


class TagBase(SQLModel):
    name: str = Field(max_length=64)
    tasks: List[Task] = Relationship(back_populates='tag', link_model=TaskTagLink)



class TagCreate(TagBase):
    pass


class TagUpdate(SQLModel):
    name: Optional[str] = Field(default=None, max_length=64)

class Tag(TagBase, table=True):
    id: int = Field(default=None, primary_key=True)

    def update(self, tag: TagCreate):
        for key, value in tag.__dict__.items():
            setattr(self, key, value)



