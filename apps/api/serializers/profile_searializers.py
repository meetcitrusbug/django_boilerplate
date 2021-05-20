from rest_framework import fields, serializers
from reg_website.models import User
from rest_framework.authtoken.models import Token


class ChangeProfileSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id','token', 'first_name', 'last_name','address']

        extra_kwargs = {"password":
                            {"write_only": True}
                        }

    def get_token(self, obj):
        return f"Token {Token.objects.get_or_create(user=obj)[0]}"



class GetProfileSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'token', 'email', 'username', 'first_name', 'last_name', 'phone' ,'address']

    def get_token(self, obj):
        return f"Token {Token.objects.get_or_create(user=obj)[0]}"
