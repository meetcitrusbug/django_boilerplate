"""
This is a Serializer module.
Define your custom serializers here.
"""
from rest_framework import serializers, status
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """
    class Meta:
        model = UserModel
        fields = (
            'id',
            'username',
            'email',
            'apple_token',
            'is_active',
        )


class JwtSerializer(serializers.Serializer):
    """
    Serializer for JWT authentication.
    """
    token = serializers.CharField()
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        """
        Required to allow using custom USER_DETAILS_SERIALIZER in
        JWTSerializer. Defining it here to avoid circular imports
        """

        user_data = UserDetailsSerializer(obj['user'], context=self.context).data

        return user_data
