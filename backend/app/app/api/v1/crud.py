from fastapi import APIRouter
from app.db import get_session
from app.models.users import User, UserCreate, UserUpdate
from app.models.tasks import Task, TaskCreate, TaskUpdate
from app.models.tasks import Tag, TagCreate, TagUpdate
from app.utils.crud import CRUDRouterFactory, CRUDFactorySettings

factory = CRUDRouterFactory()
user_crud = factory.build(
    CRUDFactorySettings(
        name='user', 
        schema=UserCreate, 
        update_schema=UserUpdate, 
        db_model=User, 
        db_conn=get_session
    )
)
task_crud = factory.build(
    CRUDFactorySettings(
        name='task',
        schema=TaskCreate,
        update_schema=TaskUpdate,
        db_model=Task,
        db_conn=get_session
    )
)
tag_crud = factory.build(
    CRUDFactorySettings(
        name='tag',
        schema=TagCreate,
        update_schema=TagUpdate,
        db_model=Tag,
        db_conn=get_session
    )
)


router = APIRouter()
router.include_router(user_crud)
router.include_router(task_crud)
router.include_router(tag_crud)
