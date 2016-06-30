# coding:utf-8
from django import forms
from db.models import *


class Register(forms.Form):
    username = forms.CharField(max_length=255, required=False, db_index=True, label='用户名')
    phone = forms.CharField(max_length=255, required=False, label='手机号')
    password = forms.CharField(max_length=255, required=False, label='密码')
    again_password = forms.CharField(max_length=255, required=False, label='确认密码')
    identify_code = forms.CharField(max_length=255, required=False, label='验证码')

    def clean_username(self):
        username = self.cleaned_data['username']
        # password = self.cleaned_data['password']
        # again_password = self.cleaned_data['again_password']

        customer_username = Register.objects.filter(username=username)