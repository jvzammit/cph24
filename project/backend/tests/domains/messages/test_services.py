from unittest import mock

import pytest

from backend.domains.messages.dependencies import (
    get_conversation_repository,
    get_suggestions_service,
)
from backend.domains.messages.models import WebhookPayload
from backend.domains.messages.repositories import ConversationRepository
from backend.domains.messages.services import SuggestionsService, WebhookService
from backend.tests.conftest import override_dependency


@pytest.fixture
def mock_conversation_repository():
    conversation_repository = mock.AsyncMock(autospec=ConversationRepository)

    def mock_get_conversation_repository():
        return conversation_repository

    with override_dependency(
        get_conversation_repository, mock_get_conversation_repository
    ):
        yield conversation_repository


@pytest.fixture
def mock_suggestions_service():
    suggestions_service = mock.AsyncMock(autospec=SuggestionsService)

    def mock_get_suggestions_service():
        return suggestions_service

    with override_dependency(get_suggestions_service, mock_get_suggestions_service):
        yield suggestions_service


class WebhookServiceTests:
    async def test_handle_webhook_request(
        self, mock_conversation_repository, mock_suggestions_service
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
        # And conversation returned by mock conversation repository
        mock_conversation = mock.Mock()
        mock_conversation_repository.handle_webhook_payload.return_value = (
            mock_conversation
        )
        # And service instance
        service = WebhookService(mock_conversation_repository, mock_suggestions_service)

        # When function is called
        await service.handle_webhook_request(payload=payload)

        # Then webhook payload is handled by repository
        mock_conversation_repository.handle_webhook_payload.assert_has_calls(
            [mock.call(payload)]
        )
        # And conversation returned by repository is posted to suggestions service
        mock_suggestions_service.post_to_service.assert_has_calls(
            [mock.call(mock_conversation)]
        )
