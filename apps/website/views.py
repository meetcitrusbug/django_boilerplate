from django.shortcuts import render

def home(request):
    return render(request, 'website/index.html')

def login(request):
    return render(request, 'website/login.html')
