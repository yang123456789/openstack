#-*- coding:utf-8 -*-

from db.views import *
from db.models import Register
import requests
import json
import re

def index(request):
    params = request.POST
    result, message = registered(params)
    if result:
        openstack = Register(
            customer_username = params['username'],
            customer_phone = params['phone'],
            customer_password = params['password'],
            customer_again_password = params['new_password'],
            identify_code = params['identify_code'],
        )
    openstack.save()
    return render(request, 'homepage/login.html')

def registered(params):
    if len(params.get('username')) < 1:
        return False, "username is invalid"
    if params['phone'].isdigit() is False:
        return False, "phone is invalid"
    if len(params.get('password')) < 1:
        return False, "password is invalid"
    if len(params.get('new_password')) < 1:
        return False, "newpassword is invalid"
    if len(params.get('identify_code')) < 1:
        return False, "identitycode is invalid"
    return True, "success"

def resigter(request):
    return render(request, 'homepage/register.html')
