from fastapi import FastAPI

from app.database.connection import engine, Base
from app.routers import employee

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employee CRUD API",
    description="Employee Create, Read, Update and Delete API",
    version="1.0.0"
)

# Register router
app.include_router(employee.router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Employee CRUD API"
    }