from rest_framework import fields, serializers
from reg_website.models import User
from rest_framework.authtoken.models import Token


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(read_only=True, required=False)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'password', 'confirm_password', 'phone']

        extra_kwargs = {"password":
                            {"write_only": True}
                        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'phone', 'token']

    def get_token(self, obj):
        return f"Token {Token.objects.get_or_create(user=obj)[0]}"
