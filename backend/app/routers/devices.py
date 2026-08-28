from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database import get_db
from backend.app.models import Bot
from backend.app.schemas import (
    BotRegisterRequest,
    BotRegisterResponse,
    BotStatusResponse,
)


router = APIRouter(
    prefix="/api/v1/devices",
    tags=["Devices"],
)


@router.post(
    "/register",
    response_model=BotRegisterResponse,
)
def register_device(
    bot_data: BotRegisterRequest,
    db: Session = Depends(get_db),
):
    existing_bot = (
        db.query(Bot)
        .filter(Bot.bot_id == bot_data.bot_id)
        .first()
    )

    if existing_bot:
        return existing_bot

    new_bot = Bot(
        bot_id=bot_data.bot_id,
        name=bot_data.name,
        status="offline",
    )

    db.add(new_bot)
    db.commit()
    db.refresh(new_bot)

    return new_bot


@router.get(
    "/{bot_id}/status",
    response_model=BotStatusResponse,
)
def get_device_status(
    bot_id: str,
    db: Session = Depends(get_db),
):
    bot = (
        db.query(Bot)
        .filter(Bot.bot_id == bot_id)
        .first()
    )

    if not bot:
        raise HTTPException(
            status_code=404,
            detail="Bot not found",
        )

    return bot


@router.post(
    "/{bot_id}/heartbeat",
    response_model=BotStatusResponse,
)
def heartbeat(
    bot_id: str,
    db: Session = Depends(get_db),
):
    bot = (
        db.query(Bot)
        .filter(Bot.bot_id == bot_id)
        .first()
    )

    if not bot:
        raise HTTPException(
            status_code=404,
            detail="Bot not found",
        )

    bot.status = "online"
    bot.last_seen = datetime.now(timezone.utc)
    bot.updated_at = datetime.now(timezone.utc)

    db.commit()
    db.refresh(bot)

    return bot