from twilio.rest import Client

TWILIO_SID = "ACd55ae8e7eb2fff7d7e2fc38ea8ed73c6"
TWILIO_AUTH_TOKEN = "986ffeed5b92d191673b171a82f9ef08"
TWILIO_VIRTUAL_NUMBER = "+13023435251"
TWILIO_VERIFIED_NUMBER = "+91 79901 17767"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)