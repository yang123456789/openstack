#-*- coding:utf-8 -*-

from db.views import *
from db.models import Register
import requests
import json
from portal import sshkey

def index(request):
    params = request.POST
    result, message = _registered(params)
    if result:
        ssh_public_key = sshkey.generation_two_keys(
        params['username'].encode('utf-8'),
        params['password'].encode('utf-8')
        )
        token = sshkey.validation(ssh_public_key)

        openstack = Register(
            customer_username = params['username'],
            customer_phone = params['phone'],
            customer_password = params['password'],
            customer_again_password = params['new_password'],
            identify_code = params['identify_code'],
            auth_token = token,
        )
    openstack.save()
    return render(request, 'homepage/login.html')

def _registered(params):
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
