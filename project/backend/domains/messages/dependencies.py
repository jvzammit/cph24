from backend.domains.messages.repositories import ConversationRepository
from backend.domains.messages.services import SuggestionsService, WebhookService
from fastapi import Depends


def get_conversation_repository() -> ConversationRepository:
    return ConversationRepository()


def get_suggestions_service() -> SuggestionsService:
    return SuggestionsService()


def get_webhook_service(
    conversation_repository: ConversationRepository = Depends(
        get_conversation_repository
    ),
    suggestions_service: SuggestionsService = Depends(get_suggestions_service),
) -> WebhookService:
    return WebhookService(
        conversation_repository=conversation_repository,
        suggestions_service=suggestions_service,
    )
