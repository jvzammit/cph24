import logging

from backend.domains.messages.models import Conversation, WebhookPayload
from backend.domains.messages.repositories import ConversationRepository

logger = logging.getLogger(__name__)


class SuggestionsService:
    async def post_to_service(self, conversation: Conversation) -> None:
        """
        Makes network I/O bound call to suggestions service with full conversation

        Args:
            conversation (Conversation): conversation posted to suggestions service
        """
        logger.debug(conversation.model_dump_json())


class WebhookService:
    def __init__(
        self,
        conversation_repository: ConversationRepository,
        suggestions_service: SuggestionsService,
    ):
        self._conversation_repository = conversation_repository
        self._suggestions_service = suggestions_service

    async def handle_webhook_request(self, payload: WebhookPayload) -> None:
        conversation = await self._conversation_repository.handle_webhook_payload(
            payload
        )
        await self._suggestions_service.post_to_service(conversation)
