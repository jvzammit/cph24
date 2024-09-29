import arrow

from django.test import TestCase

from agents.tests.factories import ConversationFactory, MessageFactory


class ConversationTests(TestCase):
    def test_str(self):
        # Given conversation with preset timestamp
        conversation = ConversationFactory(
            external_id="f47ac10b-58cc-4372-a567-0e02b2c3d479",
            timestamp=arrow.get("2024-10-04 09:45:58").datetime,
        )
        expected = "f47ac10b-58cc-4372-a567-0e02b2c3d479 - 2024-10-04 09:45:58"

        # When conversation is converted to str
        result = str(conversation)

        # Then result is as expected
        self.assertEqual(result, expected)


class MessageTests(TestCase):
    def test_str(self):
        # Given message
        message = MessageFactory(
            external_id="f47ac10b-58cc-4372-a567-0e02b2c3d479",
            timestamp=arrow.get("2024-10-04 09:45:58").datetime,
        )
        expected = (
            "f47ac10b-58cc-4372-a567-0e02b2c3d479 - inbound - 2024-10-04 09:45:58"
        )

        # When message is converted to str
        result = str(message)

        # Then result is as expected
        self.assertEqual(result, expected)
