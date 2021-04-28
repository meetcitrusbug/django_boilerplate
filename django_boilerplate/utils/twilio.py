"""
Define your Twilio service related stuff here.
"""

from django.conf import settings
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client


def send_sms(phone, text):
    """
    This method send a text SMS to specified phone number.
    """
    account_sid = settings.ACCOUNT_SID  # os.getenv("ACCOUNT_SID", "ACbfa61a1b125390190d32526bc183b27d")
    auth_token = settings.AUTH_TOKEN  # os.getenv("TWILIO_AUTH_TOKEN", "eb9ea79b7fbcd1022544ac53419bd338")
    from_number = settings.FROM_NUMBER

    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to=phone,
            from_=from_number,  # os.getenv("TWILIO_FORM_NUMBER", "+14192859494"),
            body=text
        )
        print(message.sid)
        return message
    except TwilioRestException as e:
        print(e)
        return str(e)
