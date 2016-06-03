from db.models import Register
from db.views import *
from portal import exception
from portal import sshkey


def validate(request):
    params = request.POST
    username = utf8(params['username'])
    vitify = Register.objects.filter(customer_username = username)
    if vitify:
        if len(vitify) > 1:
            raise exception.VitityLenException()
        else:
            for vf in vitify:
                if vf.customer_username is not None and vf.customer_password is not None:
                    ssh_public_key = sshkey.generation_two_keys(vf.customer_username, vf.customer_password)
                    auth_token = sshkey.validation(ssh_public_key)
                    if auth_token == vf.auth_token:
                        return redirect('/common')
                    else:
                        raise exception.AuthTokenVitity()
    # return render(request, 'homepage/login.html')
    # return redirect('')