from http import HTTPStatus
from unittest import mock

import pytest

from backend.domains.messages.dependencies import get_webhook_service
from backend.domains.messages.models import WebhookPayload
from backend.domains.messages.services import WebhookService
from backend.tests.conftest import override_dependency


@pytest.fixture
def mock_webhook_service():
    webhook_service = mock.AsyncMock(autospec=WebhookService)

    def mock_get_webhook_service():
        return webhook_service

    with override_dependency(get_webhook_service, mock_get_webhook_service):
        yield webhook_service


@pytest.mark.django_db
async def test_webhook(client, mock_webhook_service):
    # Given payload
    request_payload = {
        "message_id": "3fa85f64-5717-4562-b3fc-2c963f66af25",
        "conversation_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "timestamp": "2024-09-29T10:22:57.691Z",
        "direction": "outbound",
        "text": "string",
    }

    # When request is made
    response = await client.post("/api/messages/webhook", json=request_payload)

    # Then response is returned with expected status
    assert response.status_code == HTTPStatus.OK
    # And service is called with expected payload
    mock_webhook_service.handle_webhook_request.assert_has_calls(
        [mock.call(WebhookPayload(**request_payload))]
    )
