from agents import models as orm
from backend.domains.messages.models import Conversation, Message, WebhookPayload


class ConversationRepository:
    async def handle_webhook_payload(self, payload: WebhookPayload) -> Conversation:
        """
        Persists payload and returns full conversation.

        Args:
            payload (WebhookPayload): payload object to be persisted.

        Returns:
            Conversation: complete conversation after persisting message.
        """
        defaults = {"timestamp": payload.timestamp}
        orm_conversation, _ = await orm.Conversation.objects.aget_or_create(
            external_id=payload.conversation_id, defaults=defaults
        )
        await orm.Message.objects.acreate(
            conversation=orm_conversation,
            timestamp=payload.timestamp,
            external_id=payload.message_id,
            direction=payload.direction,
            text=payload.text,
        )
        return await _conversation_from_orm(orm_conversation)


async def _conversation_from_orm(orm_conversation: orm.Conversation) -> Conversation:
    messages = [
        Message(
            external_id=orm_message.external_id,
            timestamp=orm_message.timestamp,
            direction=orm_message.direction,
        )
        async for orm_message in orm_conversation.message_set.all()
    ]
    return Conversation(
        external_id=orm_conversation.external_id,
        timestamp=orm_conversation.timestamp,
        messages=messages,
    )
