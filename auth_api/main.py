from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controller import auth

app = FastAPI(title="Authentication API")

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

app.include_router(auth.router)
