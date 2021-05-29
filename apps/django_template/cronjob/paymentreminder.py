from customadmin.models import SubscriptionOrder
from django_boilerplate.template_id import SUBSCRIPTION_EXPIRATION_TEMPLATE_ID
from django_boilerplate.helper import send_html_template_email
from datetime import datetime, timedelta, date


def cronjob_for_one_week():
    subscribers_list = SubscriptionOrder.objects.filter(expire_date__date = date.today() + timedelta(7),plan_status='active')
    for user in subscribers_list:
        dynamic_data_for_template = {
            'time':'1 week'
        }
        to_email = user.user.email
        send_html_template_email(to_email, SUBSCRIPTION_EXPIRATION_TEMPLATE_ID, dynamic_data_for_template)
    return subscribers_list

def cronjob_for_two_week():
    subscribers_list = SubscriptionOrder.objects.filter(expire_date__date = date.today() + timedelta(14),plan_status='active')
    for user in subscribers_list:
        dynamic_data_for_template = {
            'time':'2 week'
        }
        to_email = user.user.email
        send_html_template_email(to_email, SUBSCRIPTION_EXPIRATION_TEMPLATE_ID, dynamic_data_for_template)
    return subscribers_list

def cronjob_for_one_month():
    subscribers_list = SubscriptionOrder.objects.filter(expire_date__date = date.today() + timedelta(31),plan_status='active')
    for user in subscribers_list:
        dynamic_data_for_template = {
            'time':'1 month'
        }
        to_email = user.user.email
        send_html_template_email(to_email, SUBSCRIPTION_EXPIRATION_TEMPLATE_ID, dynamic_data_for_template)
    return subscribers_list