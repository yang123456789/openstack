#coding:utf-8

from django.shortcuts import *

def index(request):
    return render(request, 'common/openstack.html')
