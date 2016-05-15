from django.shortcuts import render

def index(request):

    return render(request, 'homepage/login.html')

def register(request):
    return render(request, 'homepage/register.html')