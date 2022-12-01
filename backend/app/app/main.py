""" Main application logic"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import crud as v1

tags_metadata = [
    {
        "name": "users",
        "description": "API to manage User database"
    },
    {
        "name": "tasks",
        "description": "API to manage tasks"
    },
    {
        "name": "tags",
        "description": "API to manage tags"
    }
]

app = FastAPI(openapi_tags=tags_metadata)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    v1.router,
    prefix='/api/v1'
)

