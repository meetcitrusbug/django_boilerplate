from django.contrib.auth import get_user_model as my_get_user_model


def get_user_model():
    return my_get_user_model()