from db.models import Register
from db.views import *
from portal import exception
from portal import sshkey


def validate(request):
    params = request.POST
    username = params.get('username')
    password = params.get('password')
    vitify = Register.objects.filter(customer_username = username)
    for vf in vitify:
        customer_username = vf.customer_username
        customer_password = vf.customer_password
        if username == customer_username and password == customer_password:
            print vf.auth_token
        else:
            raise exception.AuthTokenVitity()
    return render(request, 'homepage/login.html')
    # return redirect('')