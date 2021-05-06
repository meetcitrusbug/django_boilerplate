from django.shortcuts import render

def home(request):
    return render(request, 'django_template/index.html')

def login(request):
    return render(request, 'django_template/login.html')
