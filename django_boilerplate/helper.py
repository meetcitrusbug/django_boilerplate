import sendgrid
import os
from sendgrid.helpers.mail import Email, Substitution, Mail, Personalization
from python_http_client import exceptions
from .settings import SENDGRID_API_KEY
from .template_id import DJANGO_BOILERPLATE_TEST_TEMPLATE_ID

# to_email - Whom to send the email
# sendgrid_temlpate_id - Template id created in the sendgrid account for different template
# dynamic_data_for_template - Format
# dynamic_data_for_template = {
#                           'variable_name_as_in_sendgrid_tempaltes': value in string format,
#                           }
# Example dynamic_data_for_template = {
            #     'name': 'Citrusbug Team',
            # }

def send_html_template_email(to_email, sendgrid_temlpate_id, dynamic_data_for_template):
    print(to_email, sendgrid_temlpate_id, dynamic_data_for_template)
    sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)
    personalization = Personalization()
    personalization.add_to(Email(to_email))
    mail = Mail()
    mail.from_email = Email("citrusbugteam@gmail.com")
    mail.template_id = sendgrid_temlpate_id
    personalization.dynamic_template_data = dynamic_data_for_template
    mail.add_personalization(personalization)
    try:
        response = sg.client.mail.send.post(request_body=mail.get())
    except exceptions.BadRequestsError as e:
        print(e.body)
        exit()