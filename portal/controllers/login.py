from db.models import Register
from db.views import *
from portal import exception
from portal import sshkey
from django.http import HttpResponse


def validate(request):
    params = request.POST
    username = params['username']
    password = params['password']
    vitify = Register.objects.filter(customer_username = username)
    if len(vitify) == 1:
        for vf in vitify:
            customer_username = vf.customer_username
            customer_password = vf.customer_password
            if username == customer_username and password == customer_password:
                return redirect('/common', {'token': vf.auth_token})
            else:
                raise exception.AuthTokenVitity()
    else:
        raise exception.VitityLenException()
    # return render(request, 'homepage/login.html')
    # return redirect('')
