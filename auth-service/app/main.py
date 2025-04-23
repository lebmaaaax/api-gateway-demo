from fastapi import FastAPI
from auth import router as auth_router
from database import create_db_and_tables

app = FastAPI(
    title="Auth Service",
    description="Handles user registration, login, and JWT authentication.",
    version="1.0.0"
)

# Подключаем роуты из auth.py
app.include_router(auth_router, prefix="/auth")

# Этот код выполняется при старте приложения
@app.on_event("startup")
def on_startup():
    create_db_and_tables()