from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings
from rest_framework.response import Response
from django.utils import timezone

def send_sendgrid_email(recipient_list, data={}, template_id= ''):
    try:
        message = Mail(from_email=settings.SENDGRID_FROM_EMAIL, to_emails=[recipient_list])
        date =  timezone.now()
        data['date'] = date.strftime('%d-%m-%Y')
        message.template_id =  template_id #'d-91bbcad7c67341c38a26ccac85c89c59'
        message.dynamic_template_data = data

        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        return True
    except Exception as e:
        print("===============",e)
        return False