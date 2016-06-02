from db.models import Register
from db.views import *
from portal import exception
from portal import sshkey

def validate(request):
    params = request.POST
    username = utf8(params['username'])
    vitify = Register.objects.filter(customer_username = username)
    # print type(vitify)
    # print vitify
    if vitify:
        if len(vitify) > 1:
            raise exception.VitityLenException()
        else:
            for vf in vitify:
                return vf.customer_username, vf.customer_password
    return render(request, 'homepage/login.html')
    # return redirect('')