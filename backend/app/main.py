from fastapi import FastAPI

from backend.app.config import settings


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
    return {
        "status": "healthy",
        "bot_id": settings.bot_id,
    }