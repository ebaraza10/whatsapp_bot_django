
import pytest
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

pytestmark = pytest.mark.django_db


class BotView(APITestCase):

    def test_create_reminder(self):
        client = APIClient()

        data = {
            "SmsMessageSid": "1",
            "NumMedia": "0",
            "ProfileName": "Test user",
            "SmsSid": "001",
            "WaId": "2547XXYYYZZZ",
            "SmsStatus": "received",
            "Body": "Hello",
            "MessageSid": "001",
            "To": "whatsapp:+14155238886",
            "NumSegments": "1",
            "AccountSid": "001",
            "From": "2547XXYYYZZZ",
            "ApiVersion": "2010-04-01"
        }
        
        response = client.get('/bot/reminders/', data=data)

        assert response.status_code == 200
