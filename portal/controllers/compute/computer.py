from django.shortcuts import *


def index(request):
    return render(request, 'homepage/compute/system_info.html')