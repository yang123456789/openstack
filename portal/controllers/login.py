from db.models import Register
from db.views import *
from portal import sshkey

def validate(request):
    params = request.POST
    username = utf8(params['username'])
    vitify = Register.objects.filter(customer_username = username)
    print vitify

    if len(vitify) > 1:
        raise
    return render(request, 'homepage/login.html')
    # return redirect('')