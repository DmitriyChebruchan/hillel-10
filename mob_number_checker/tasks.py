from celery import (
    shared_task,
)
from twilio.rest import (
    Client,
)
from django.conf import (
    settings,
)

client = Client(
    settings.TWILIO_ACCOUNT_SID,
    settings.TWILIO_AUTH_TOKEN,
)


@shared_task()
def send_sms(
    receiver,
    text,
):
    message = client.messages.create(
        from_="+12516163477",
        body=text,
        to=receiver,
    )
    print(message.sid)
    return message.sid
