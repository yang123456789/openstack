from db.forms import *
from db.models import Register
from db.views import *
from django.utils.translation import ugettext as _


def index(request):
    return render(request, 'sysadmin/login.html')


def login(request):
    session = request.session
    return