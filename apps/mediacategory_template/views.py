from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from mediacategory_api.models import MediaCategory, MediaImage, MediaVideo
from django.views import View

class IndexView(View):
    def get(self, request):
        mediacategory = MediaCategory.objects.all()
        return render(request, 'mediacategory_template/index.html',{"mediacategory":mediacategory})


class LoginPageView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request=request, template_name="mediacategory_template/userlogin.html", context={"login_form":form})

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
                return redirect('login')
        else:
            return redirect('login')


def userlogout(request):
    logout(request)
    return redirect('/')


class MediaCategoryDetailView(View):
    def get(self, request, pk):
        categoryname = MediaCategory.objects.get(pk=pk)
        mediaimage = MediaImage.objects.filter(category=pk)
        mediavideo = MediaVideo.objects.filter(category=pk)
        return render(request, 'mediacategory_template/detail.html',{"categoryname":categoryname, "mediaimage":mediaimage, "mediavideo":mediavideo})