from django.db import models


class Conversation(models.Model):
    external_id = models.UUIDField(
        editable=False, unique=True, null=False, verbose_name="External ID"
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    timestamp = models.DateTimeField(
        editable=False, help_text="External platform timestamp"
    )
    # other fields here would be agent_id and visitor_id, both UUIDs

    def __str__(self) -> str:
        return f"{self.external_id} - {self.timestamp.strftime("%Y-%m-%d %H:%M:%S")}"


class MessageDirection(models.TextChoices):
    INBOUND = ("inbound", "Inbound")
    OUTBOUND = ("outbound", "Outbound")


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    external_id = models.UUIDField(
        editable=False, unique=True, null=False, verbose_name="External ID"
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    timestamp = models.DateTimeField(
        editable=False, help_text="External platform timestamp"
    )
    direction = models.CharField(max_length=16, choices=MessageDirection)
    text = models.TextField()

    def __str__(self) -> str:
        return f"{self.external_id} - {self.direction} - {self.timestamp.strftime("%Y-%m-%d %H:%M:%S")}"
