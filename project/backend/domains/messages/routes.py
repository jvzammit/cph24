from typing import Annotated

from starlette.responses import Response

from fastapi import APIRouter, Depends

from backend.domains.messages.dependencies import get_webhook_service
from backend.domains.messages.models import WebhookPayload
from backend.domains.messages.services import WebhookService

api_router = APIRouter(tags=["Messages"])


@api_router.api_route("/webhook", methods=["POST"])
async def webhook(
    payload: WebhookPayload,
    webhook_service: Annotated[WebhookService, Depends(get_webhook_service)],
) -> Response:
    await webhook_service.handle_webhook_request(payload)
    return Response(status_code=200)
