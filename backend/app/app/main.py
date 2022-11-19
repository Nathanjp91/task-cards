""" Main application logic"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import crud as v1

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(
#     v1.router,
#     prefix='/api/v1'
# )
app.include_router(
    v1.router,
    prefix='/api/v1'
)

