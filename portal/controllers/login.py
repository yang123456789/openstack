from db.models import Register
from django.utils.translation import ugettext as _
from portal.views import *
import StringIO


def index(request):
    return render(request, 'sysadmin/login.html')


def login(request):
    session = request.session
    return


def get_login(request):
    params = request.GET
    username = params.get('username').encode('utf-8')
    password = params.get('password')
    login_check = {}
    if (username is not None or username != 'null' and
        password is not None or password != 'null'):
        username_password = {'data': str(_login_check(username))}
        login_check.update(username_password)
    return render_json(login_check)


def _login_check(username):
    username = Register.objects.filter(username__iexact=username)
    if len(username) == 1:
        return username


def generate_captcha(request):
    mstream = StringIO.StringIO()
    validate_codes = create_identify_code()
    img = validate_codes[0]
    img.save(mstream, "GIF")

    # Save the verification code to session
    request.session['validate_code'] = validate_codes[1]
    return HttpResponse(mstream.getvalue())


def validate_code(request):

    return render_json()
