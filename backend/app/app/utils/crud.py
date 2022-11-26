from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import SQLModel
from typing import Callable, Union, List, Any, Optional
from pydantic import BaseSettings, BaseModel


class RouteSettings(BaseModel):
    include: bool = True
    dependencies: List[Callable[..., Any]] = []
    function_override: Optional[Callable[..., APIRouter]] = None


class CRUDFactorySettings():
    name: str
    schema: SQLModel
    update_schema: SQLModel
    db_model: SQLModel
    db_conn: AsyncSession
    tags: Optional[List[str]] = None
    post: RouteSettings = RouteSettings()
    get: RouteSettings = RouteSettings()
    get_all: RouteSettings = RouteSettings()
    update: RouteSettings = RouteSettings()
    delete: RouteSettings = RouteSettings()
    
    def __init__(
        self,
        name: str,
        schema: SQLModel,
        update_schema: SQLModel,
        db_model: SQLModel,
        db_conn: AsyncSession,
        tags: Optional[List[str]]=None,
        post: Union[RouteSettings, None]=None,
        get: Union[RouteSettings, None]=None,
        get_all: Union[RouteSettings, None]=None,
        update: Union[RouteSettings, None]=None,
        delete: Union[RouteSettings, None]=None
    ):
        if post:
            self.post = post
        if get:
            self.get = get
        if get_all:
            self.get_all = get_all
        if update:
            self.update = update
        if delete:
            self.delete = delete
        
        self.update_schema = update_schema
        self.name = name
        self.schema = schema
        self.db_model = db_model
        self.db_conn = db_conn
        self.tags = tags if tags else [name + 's']


class CRUDRouterFactory():
    def build(self,
              settings: CRUDFactorySettings
    ) -> APIRouter:
        router = APIRouter()

        router = self._build_create(router, settings)
        router = self._build_get(router, settings)
        router = self._build_get_all(router, settings)
        router = self._build_update(router, settings)
        router = self._build_delete(router, settings)
        
        return router
    
    def _build_get_all(self,
                       router: APIRouter,
                       settings: CRUDFactorySettings
    ) -> APIRouter:
        if not settings.get_all.include:
            return router

        if settings.get_all.function_override:
            router.get(f"/{settings.name}/")(settings.get.function_override)
            return router
            
        @router.get(f"/{settings.name}", tags=settings.tags)
        async def get_all(session: AsyncSession = Depends(settings.db_conn)) -> List[settings.db_model]:
                models = await session.execute(select(settings.db_model))
                print(models)
                if not models:
                    raise HTTPException(status_code=404, detail=f"{settings.name}s not found")
                return models.all()
        return router
    
    
    def _build_get(self,
                   router: APIRouter,
                   settings: CRUDFactorySettings
    ) -> APIRouter:
        if not settings.get.include:
            return router

        if settings.get.function_override:
            router.get(f"/{settings.name}/{{id}}")(settings.get.function_override)
            return router
            
        @router.get(f"/{settings.name}/{{id}}", tags=settings.tags)
        async def get_with_id(id: int, session: AsyncSession = Depends(settings.db_conn)) -> settings.db_model:
                model = await session.get(settings.db_model, id)
                if not model:
                    raise HTTPException(status_code=404, detail=f"{settings.name} not found")
                return model
        return router
    
    
    def _build_create(self,
                      router: APIRouter,
                      settings: CRUDFactorySettings
    ) -> APIRouter:
        if not settings.post.include:
            return router

        if settings.post.function_override:
            router.post(f"/{settings.name}")(settings.post.function_override)
            return router
            
        @router.post(f"/{settings.name}", tags=settings.tags)
        async def create(model: settings.schema, session: AsyncSession = Depends(settings.db_conn)) -> settings.db_model:
            db_model = model.into_db_model()
            session.add(db_model)
            await session.commit()
            await session.refresh(db_model)
            return db_model
        return router
    
    
    def _build_update(self,
                      router: APIRouter,
                      settings: CRUDFactorySettings
    ) -> APIRouter:
        if not settings.post.include:
            return router

        if settings.post.function_override:
            router.patch(f"/{settings.name}/{{id}}")(settings.update.function_override)
            return router
            
        @router.patch(f"/{settings.name}/{{id}}", tags=settings.tags)
        async def update_with_id(id: int, model: settings.update_schema, session: AsyncSession = Depends(settings.db_conn)):
            db_model = await session.get(settings.db_model, id)
            if not db_model:
                raise HTTPException(status_code=404, detail=f"{settings.name}s not found")
            model_data = model.dict(exclude_unset=True)
            for key, value in model_data.items():
                setattr(db_model, key, value)
            session.add(db_model)
            await session.commit()
            await session.refresh(db_model)
            return db_model
        return router
    
    
    def _build_delete(self,
                      router: APIRouter,
                      settings: CRUDFactorySettings
    ) -> APIRouter:
        if not settings.post.include:
            return router

        if settings.post.function_override:
            router.delete(f"/{settings.name}/{{id}}")(settings.delete.function_override)
            return router
            
        @router.delete(f"/{settings.name}/{{id}}", tags=settings.tags)
        async def delete_with_id(id: int, session: AsyncSession = Depends(settings.db_conn)):
            db_model = await session.get(settings.db_model, id)
            if not db_model:
                raise HTTPException(status_code=404, detail=f"{settings.name}s not found")
            await session.delete(db_model)
            await session.commit()
            return {id: "Deleted"}
        return router
    