# Generated by Django 5.1.1 on 2024-09-28 11:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Conversation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "external_id",
                    models.UUIDField(
                        editable=False, unique=True, verbose_name="External ID"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "timestamp",
                    models.DateTimeField(
                        editable=False, help_text="External platform timestamp"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "external_id",
                    models.UUIDField(
                        editable=False, unique=True, verbose_name="External ID"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "timestamp",
                    models.DateTimeField(
                        editable=False, help_text="External platform timestamp"
                    ),
                ),
                (
                    "direction",
                    models.CharField(
                        choices=[("inbound", "Inbound"), ("outbound", "Outbound")],
                        max_length=16,
                    ),
                ),
                ("text", models.TextField()),
                (
                    "conversation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="agents.conversation",
                    ),
                ),
            ],
        ),
    ]
