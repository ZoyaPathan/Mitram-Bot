from datetime import datetime

from pydantic import BaseModel


class BotRegisterRequest(BaseModel):
    bot_id: str
    name: str


class BotRegisterResponse(BaseModel):
    id: int
    bot_id: str
    name: str
    status: str
    created_at: datetime
    updated_at: datetime