from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_session
from fastapi_crudrouter import SQLAlchemyCRUDRouter as CRUDRouter
from app.models.users import User, UserCreate, UserBase
from app.models.tasks import Task, TaskCreate, TaskBase
from app.models.tasks import Tag, TagCreate, TagBase

router = APIRouter()

tag_router = CRUDRouter(
    schema=TagBase,
    create_schema=TagCreate,
    db_model=Tag,
    db=get_session
)

user_router = CRUDRouter(
    schema=UserBase,
    create_schema=UserCreate,
    db_model=User,
    db=get_session
)

task_router = CRUDRouter(
    schema=TaskBase,
    create_schema=TaskCreate,
    db_model=Task,
    db=get_session
)

router.include_router(tag_router)
router.include_router(user_router)
router.include_router(task_router)

# @router.post("/user")
# async def create_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
#     user = User(email=user.email, password=user.password, admin=user.admin)
#     session.add(user)
#     await session.commit()
#     await session.refresh(user)
#     return user


# @router.get("/user/{user_id}")
# async def read_user(user_id: int, session: AsyncSession = Depends(get_session)):
#     user = await session.get(User, user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user


# @router.put("/user/{user_id}")
# async def update_user(user_id: int, update: UserCreate, session: AsyncSession = Depends(get_session)):
#     user = await session.get(User, user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     user.update(update)
#     session.add(user)
#     await session.commit()
#     await session.refresh(user)
#     return user


# @router.delete("/user/{user_id}")
# async def delete_user(user_id: int, session: AsyncSession = Depends(get_session)):
#     user = await session.get(User, user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     await session.delete(user)
#     await session.commit()
#     return {user_id: "Deleted Successfully"}


# @router.post("/task")
# async def create_task(task: TaskCreate, session: AsyncSession = Depends(get_session)):
#     task = Task(email=task.email, password=task.password, admin=task.admin)
#     session.add(task)
#     await session.commit()
#     await session.refresh(task)
#     return task


# @router.get("/task/{task_id}")
# async def read_task(task_id: int, session: AsyncSession = Depends(get_session)):
#     task = await session.get(Task, task_id)
#     if not task:
#         raise HTTPException(status_code=404, detail="Task not found")
#     return task


# @router.put("/task/{task_id}")
# async def update_task(task_id: int, update: TaskCreate, session: AsyncSession = Depends(get_session)):
#     task = await session.get(Task, task_id)
#     if not task:
#         raise HTTPException(status_code=404, detail="Task not found")
#     task.update(update)
#     session.add(task)
#     await session.commit()
#     await session.refresh(task)
#     return task


# @router.delete("/task/{task_id}")
# async def delete_task(task_id: int, session: AsyncSession = Depends(get_session)):
#     task = await session.get(Task, task_id)
#     if not task:
#         raise HTTPException(status_code=404, detail="Task not found")
#     await session.delete(task)
#     await session.commit()
#     return {task_id: "Deleted Successfully"}

