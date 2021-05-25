from rest_framework.views import APIView
from ..serializers import ChangeProfileSerializer, GetProfileSerializer
from reg_website.models import User
from rest_framework import status
from django.contrib.auth import update_session_auth_hash

from django_boilerplate.helpers import custom_response, serialized_response, get_object
from django_boilerplate.permissions import IsAccountOwner


class ChangeProfileAPIView(APIView):
    serializer_class = ChangeProfileSerializer
    permission_classes = (IsAccountOwner,)

    def get(self, request):
        user = get_object(User, request.user.pk)
        if not user:
            message = "User not found!"
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)
        serializer = GetProfileSerializer(user, context={"request": request})
        message = "User Profile fetched Successfully!"
        return custom_response(True, status.HTTP_200_OK, message, serializer.data)

    def put(self, request):
        user = get_object(User,request.user.pk)
        profile_image = request.data.get('profile_image',None)
        if not user:
            message = "User not found!"
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)
        if profile_image == '' or profile_image:
            if user.profile_image:
                user.delete_profile_image()
        message = "User Profile updated successfully!"
        serializer = self.serializer_class(user, data=request.data, partial=True, context={"request": request})
        response_status, result, message = serialized_response(serializer, message)
        status_code = status.HTTP_201_CREATED if response_status else status.HTTP_400_BAD_REQUEST
        return custom_response(response_status, status_code, message, result)


class ChangePasswordAPIVIew(APIView):
    permission_classes = (IsAccountOwner,)
    def post(self, request):
        if not 'old_password' in request.data.keys():
            message = "Old Password Is required!"
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)

        if not 'new_password' in request.data.keys():
            message = "New Password Is required!"
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)
        old_password = request.data['old_password']
        new_password = request.data['new_password']
        user = request.user
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            message="Password Changed Successfully."
            return custom_response(True, status.HTTP_201_CREATED, message)
        else:
            message="Old Password Is Not Correct."
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)
