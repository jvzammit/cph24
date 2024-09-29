from datetime import datetime
from typing import Literal
from uuid import UUID

from pydantic import BaseModel

from agents import models as orm


class Message(BaseModel):
    external_id: UUID
    timestamp: datetime
    direction: Literal[orm.MessageDirection.INBOUND, orm.MessageDirection.OUTBOUND]


class Conversation(BaseModel):
    external_id: UUID
    timestamp: datetime
    messages: list[Message] = []


class WebhookPayload(BaseModel):
    message_id: UUID
    conversation_id: UUID
    timestamp: datetime
    direction: Literal[orm.MessageDirection.INBOUND, orm.MessageDirection.OUTBOUND]
    text: str
