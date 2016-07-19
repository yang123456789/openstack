from django.shortcuts import *


def index(request):
    return render(request, 'common/../../template/sysadmin/openstack.html')