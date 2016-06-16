from django.shortcuts import render,render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.template.context import RequestContext

from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.contrib.auth.decorators import login_required

from db.models import Register
from db.forms import LoginForm
from db.views import *
from portal import exception
from portal import sshkey
from django.http import HttpResponse
import json


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
                return HttpResponseRedirect('/login')
                # raise exception.AuthTokenVitity()
                # error = {'AuthTokenVitity':'AuthToken vititied invalid'}
                # return HttpResponse(json.dumps(error), content_type='application/json')
    else:
        raise exception.VitityLenException()
    # return render(request, 'sysadmin/login.html')
    # return redirect('')


def login(request):
    if request.method == 'POST':
        form = LoginForm()
        return render(request, 'sysadmin/login.html', RequestContext(request,{'form':form,}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request,user)
                return render_to_response('index.html', RequestContext(request))
            else:
                return render(request, 'sysadmin/login.html', RequestContext(request,{'form':form,'password_is_wrong':True}))
        else:
            return render(request, 'sysadmin/login.html',RequestContext(request,{'form':form,}))


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/accounts/login/")