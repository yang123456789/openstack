from db.models import Register
from db.views import *
from portal import sshkey

def validate(request):
    params = request.POST
    # print params
    username = params['username'].encode('utf-8')
    # print username
    vitify = Register.objects.filter(customer_username = username)
    print vitify
    # for key, value in vitify.iteritems():
    #     print key.encode('utf-8'), value.encode('utf-8')
    return render(request, 'homepage/login.html')
    # return redirect('')