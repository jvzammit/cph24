import uuid

import factory
from agents.models import MessageDirection
from django.utils import timezone


class ConversationFactory(factory.django.DjangoModelFactory):
    external_id = uuid.uuid4()
    timestamp = timezone.now()

    class Meta:
        model = "agents.Conversation"
        django_get_or_create = ["external_id"]


class MessageFactory(factory.django.DjangoModelFactory):
    conversation = factory.SubFactory(ConversationFactory)
    direction = MessageDirection.INBOUND
    external_id = uuid.uuid4()
    timestamp = timezone.now()

    class Meta:
        model = "agents.Message"
        django_get_or_create = ["external_id"]
