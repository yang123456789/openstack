from db.views import *
from db.forms import RegisterForm
from db.models import Register
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError
import re
import json
from portal import sshkey


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


def register(request):
    if request.method == 'POST':
        params = request.POST
        ssh_public_key = sshkey.generation_two_keys(params['username'], params['password'])
        token = sshkey.validation(ssh_public_key)
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            phone =form.cleaned_data['phone']
            password = form.cleaned_data['password']
            again_password = form.cleaned_data['again_password']
            identify_code = form.cleaned_data['identify_code']
            res = Register.objects.create(
                auth_token=token,
                username=username,
                phone=phone,
                password=password,
                again_password=again_password,
                identify_code=identify_code,
            )
            res.save()
            return HttpResponseRedirect('/common')
    else:
        form = RegisterForm()
    return render(request, 'sysadmin/register.html', {'form': form})


def clean_username(username):
    customer_username = Register.objects.filter(username__exact=username)
    if username == customer_username:
        raise ValidationError(_('username has been used'))