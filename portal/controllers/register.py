from db.views import *
from portal.views import create_identify_code
from db.forms import RegisterForm
from db.models import Register
from portal import sshkey
import StringIO


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
            return HttpResponseRedirect('/?')
    else:
        form = RegisterForm()
    return render(request, 'sysadmin/register.html', {'form': form})


def validate_code(request):
    mstream = StringIO.StringIO()
    validate_codes = create_identify_code()
    img = validate_codes[0]
    img.save(mstream, "GIF")

    # Save the verification code to session
    request.session['validate_code'] = validate_codes[1]
    return HttpResponse(mstream.getvalue())
