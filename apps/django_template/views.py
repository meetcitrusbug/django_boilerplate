from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from notification.models import Notification, GroupUser
from django.views import View

class IndexView(View):
    def get(self, request):
        notifications = Notification.objects.filter(user=request.user.pk)
        unread_notification = Notification.objects.filter(user=request.user.pk, is_read=False).count()
        all_notification = Notification.objects.filter(user=request.user.pk).count()
        return render(request, 'django_template/index.html',{"notifications":notifications, 'unread_notification':unread_notification, 'all_notification':all_notification})


class LoginPageView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request=request, template_name="django_template/userlogin.html", context={"login_form":form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('/')
            else:
                return redirect('userlogin')
        else:
            return redirect('userlogin')


def userlogout(request):
    logout(request)
    return redirect('/')


class UserReadView(View):
    def get(self, request, pk):
        Notification.objects.filter(pk=pk).update(is_read=True)
        return redirect('/')


class UserReadAllView(View):
    def get(self, request):
        Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
        return redirect('/')


class UserRemoveView(View):
    def get(self, request, pk):
        removable = Notification.objects.filter(pk=pk)
        removable.delete()
        return redirect('/')


class UserRemoveAllView(View):
    def get(self, request):
        removable = Notification.objects.filter(user=request.user)
        removable.delete()
        return redirect('/')
