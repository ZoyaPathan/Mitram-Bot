from fastapi import FastAPI

from backend.app.config import settings
from backend.app.database import engine


app = FastAPI(
    title=settings.app_name,
    description="Backend API for the MITRAM elderly care robot",
    version=settings.app_version,
)


@app.get("/")
def root():
    return {
        "message": "MITRAM Bot Backend is running!",
        "bot_id": settings.bot_id,
        "environment": settings.environment,
    }


@app.get("/health")
def health_check():
    database_status = "connected"

    try:
        connection = engine.connect()
        connection.close()
    except Exception:
        database_status = "disconnected"

    return {
        "status": "healthy",
        "bot_id": settings.bot_id,
        "database": database_status,
    }