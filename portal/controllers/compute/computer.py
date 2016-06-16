from django.shortcuts import *


def index(request):
    return render(request, 'sysadmin/compute/system_info.html')