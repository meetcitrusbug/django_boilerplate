from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import update_session_auth_hash
from django.views import View
from django.http import JsonResponse
from ..models import User


class ChangeProfileView(View):
    template_name = 'profile_change/update-profile.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'Title': "Update Profile", 'user': request.user})

    def post(self, request):
        if request.user.is_authenticated:
            user = request.user

        if user:
            print(user.id)
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            address = request.POST['address']
            user = User.objects.filter(id = user.id)[0]
            user.first_name = first_name
            user.last_name = last_name
            user.address = address
            user.save()
            response = {
                "message": "Profile Has Been Changed.",
                "status": True
            }
            return JsonResponse(response)


class ChangePasswordView(TemplateView):
    template_name = 'profile_change/change-password.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'Title': "Change Password"})

    def post(self, request):
        old_password = request.POST.get('old_password')
        print(old_password)
        new_password = request.POST.get('new_password')
        if request.user.is_authenticated:
            user = request.user
            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                response = {
                    "message": "Password Changed Successfully.",
                    "status": True
                }
                return JsonResponse(response)
            else:
                response = {
                    "message": "Old Password Is Not Correct.",
                    "status": False
                }
                return JsonResponse(response)
        else:
            response = {
                "message": "Not Authenticated User.",
                "status": False
            }
            return JsonResponse(response)

