import asyncio

import pytest

from agents import models as orm
from agents.tests.factories import ConversationFactory, MessageFactory
from backend.domains.messages.models import WebhookPayload
from backend.domains.messages.repositories import ConversationRepository


@pytest.mark.django_db(transaction=True)
class ConversationRepositoryTests:
    def test_handle_webhook_payload_conversation_exists_reuses_conversation(self):
        # Given payload
        request_payload = {
            "message_id": "3fa85f64-5717-4562-b3fc-2c963f66af25",
            "conversation_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "timestamp": "2024-09-29T10:22:57.691Z",
            "direction": "outbound",
            "text": "string",
        }
        payload = WebhookPayload(**request_payload)
        # Given payload conversation with external_id exists
        conversation = ConversationFactory(
            external_id=request_payload["conversation_id"]
        )
        # And already a message
        MessageFactory(conversation=conversation)
        # Given repository
        repository = ConversationRepository()

        # When function is called
        conversation = asyncio.run(repository.handle_webhook_payload(payload=payload))

        # Then conversation is returned including newly-added message
        assert len(conversation.messages) == 2
        assert payload.message_id in [
            message.external_id for message in conversation.messages
        ]
        # And no new conversation was added
        assert orm.Conversation.objects.count() == 1

    def test_handle_webhook_payload_conversation_does_not_exist_creates_conversation(
        self,
    ):
        # Given payload
        request_payload = {
            "message_id": "3fa85f64-5717-4562-b3fc-2c963f66af25",
            "conversation_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "timestamp": "2024-09-29T10:22:57.691Z",
            "direction": "outbound",
            "text": "string",
        }
        payload = WebhookPayload(**request_payload)
        # Given repository
        repository = ConversationRepository()

        # When function is called
        conversation = asyncio.run(repository.handle_webhook_payload(payload=payload))

        # Then conversation is returned including newly-added message
        assert len(conversation.messages) == 1
        assert payload.message_id == conversation.messages[0].external_id
