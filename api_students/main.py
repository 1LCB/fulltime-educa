from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controller import students
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/api/student/picture", StaticFiles(directory="app/uploads"), name="pictures")

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

app.include_router(students.router)