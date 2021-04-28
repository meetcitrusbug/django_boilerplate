"""
Define firebase related functions here.
"""

import os

import firebase_admin
from django.conf import settings
from firebase_admin import credentials, messaging

from core.models import Notification

# https://github.com/firebase/firebase-admin-python/blob/f43e6876684d2c7e9acf5b0b013642b44883c63a/snippets/messaging/cloud_messaging.py#L24-L40
# https://firebase.google.com/docs/cloud-messaging/send-message#python


class Firebase():
    """
    This is a main Firebase class which includes different methods
    like send_to_token, send_to_topic, subscribe_to_topic, send_multicast etc.

    Using these methods we can send push notifications to user.
    """

    def __init__(self):
        """This method initializes the Firebase App using app-certificate"""
        json_path = os.path.join(settings.ROOT_DIR, "onedropmedia-58bb6-firebase-adminsdk-38r8o-a149a8986d.json")
        # cred = self.credentials.Certificate(json_path)
        # self.initialize_app(cred)

        if not firebase_admin._apps:
            cred = credentials.Certificate(json_path)
            firebase_admin.initialize_app(cred)

    def send_to_token(self, token, data, title, body, user):
        """This method is used to send notification to single token"""

        # [START send_to_token]
        # This registration token comes from the client FCM SDKs.
        # token = 'YOUR_REGISTRATION_TOKEN'

        # See documentation on defining a message payload.
        if not token:
            return False
        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            data=data,
            token=token,
        )

        # Send a message to the device corresponding to the provided
        # registration token.
        try:
            response = messaging.send(message)
            # Response is a message ID string.
            print('Successfully sent message:', response)

            data = {
                'user': user,
                'title': title,
                'message': body,
                'data': data,
            }
            Notification.objects.create(**data)
            return response
        except Exception as inst:
            print(inst)
            return False
        # [END send_to_token]

    def send_to_topic(self, topic, data, title, body):
        """This method is used to send notification to a topic"""
        # [START send_to_topic]
        # The topic name can be optionally prefixed with "/topics/".
        # topic = 'highScores'

        # See documentation on defining a message payload.
        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            data=data,
            topic=topic,
        )

        # Send a message to the devices subscribed to the provided topic.
        response = messaging.send(message)
        # Response is a message ID string.
        print('Successfully sent message:', response)
        return response
        # [END send_to_topic]

    def send_to_condition(self, condition, data, title, body):
        """This method is used to send notification to a topic with condition"""
        # [START send_to_condition]
        # Define a condition which will send to devices which are subscribed
        # to either the Google stock or the tech industry topics.
        # condition = "'stock-GOOG' in topics || 'industry-tech' in topics"

        # See documentation on defining a message payload.
        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            data=data,
            condition=condition,
        )

        # Send a message to devices subscribed to the combination of topics
        # specified by the provided condition.
        response = messaging.send(message)
        # Response is a message ID string.
        print('Successfully sent message:', response)
        return response
        # [END send_to_condition]

    def subscribe_to_topic(self, topic, token):
        """This method is used to subscribe a user to specific topic"""
        # topic = 'highScores'
        # [START subscribe]
        # These registration tokens come from the client FCM SDKs.
        # registration_tokens = [
        #     'YOUR_REGISTRATION_TOKEN_1',
        #     # ...
        #     'YOUR_REGISTRATION_TOKEN_n',
        # ]

        registration_tokens = [
            token,
        ]

        # Subscribe the devices corresponding to the registration tokens to the
        # topic.
        response = messaging.subscribe_to_topic(registration_tokens, topic)
        # See the TopicManagementResponse reference documentation
        # for the contents of response.
        print(response.success_count, 'tokens were subscribed successfully')
        return response
        # [END subscribe]

    def unsubscribe_from_topic(self, topic, token):
        """This method is used to unsubscribe a user from specific topic"""
        # topic = 'highScores'
        # [START unsubscribe]
        # These registration tokens come from the client FCM SDKs.
        registration_tokens = [
            token,
        ]

        # Unubscribe the devices corresponding to the registration tokens from the
        # topic.
        response = messaging.unsubscribe_from_topic(registration_tokens, topic)
        # See the TopicManagementResponse reference documentation
        # for the contents of response.
        print(response.success_count, 'tokens were unsubscribed successfully')
        return response
        # [END unsubscribe]

    def send_multicast(self, tokens, data, title, body):
        """This method is used to send notification to multiple tokens"""
        # [START send_multicast]
        # Create a list containing up to 500 registration tokens.
        # These registration tokens come from the client FCM SDKs.
        # registration_tokens = [
        #     'YOUR_REGISTRATION_TOKEN_1',
        #     # ...
        #     'YOUR_REGISTRATION_TOKEN_N',
        # ]

        message = messaging.MulticastMessage(
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            data=data,
            tokens=tokens,
        )
        response = messaging.send_multicast(message)
        # try:
        #     response = messaging.send_multicast(message)
        #     # Response is a message ID string.
        #     print('{0} messages were sent successfully'.format(response.success_count))
        #     for user in users:
        #         data = {
        #             'user': user,
        #             'title': title,
        #             'message': body,
        #             'data': data,
        #         }
        #         Notification.objects.create(**data)
        #     return response
        # except Exception as inst:
        #     print(inst)
        #     return False
        # See the BatchResponse reference documentation
        # for the contents of response.
        print('{0} messages were sent successfully'.format(response.success_count))
        # [END send_multicast]
