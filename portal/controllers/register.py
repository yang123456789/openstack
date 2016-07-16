from db.views import *
from db.forms import RegisterForm
from db.models import Register
<<<<<<< HEAD
=======
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError
import re
from portal import exception
>>>>>>> e46a9240a60209fa5abfcb06597fa39894380704
from portal import sshkey


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
            errors = []
            customer_username = Register.objects.filter(username__exact=username)
            if len(customer_username) > 1:
                errors.append(exception.UsernameException)
            if re.match(r'^\d{3}-\d{8}|\d{4}-\d{7}$|^1(3[0-9]|5[012356789]|8[0-9]|4[57]|7[68])\d{8}$', phone) == None:
                errors.append(exception.PhoneException)
            if password != again_password:
                errors.append(exception.PasswordIdentityException)
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
