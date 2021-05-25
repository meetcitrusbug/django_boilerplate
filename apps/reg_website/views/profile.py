from django.shortcuts import render
from django.views.generic import TemplateView
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
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            address = request.POST['address']
            profile_image = request.FILES.get('image')
            clear_image = request.POST.get('clear',None)
            user = User.objects.filter(id=user.id)[0]
            user.first_name = first_name
            user.last_name = last_name
            user.address = address
            if profile_image:
                if user.profile_image:
                    user.delete_profile_image()
                user.profile_image = profile_image
            else:
                if clear_image:
                    user.delete_profile_image()
                    user.profile_image = None
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
        new_password = request.POST.get('new_password')
        if request.user.is_authenticated:
            user = request.user
            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()
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

