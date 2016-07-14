# coding:utf-8
from django import forms
from db.models import *
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
import re


class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=255, required=True, label=_('username'),
        error_messages={'required': _('please input username')})
    phone = forms.CharField(
        max_length=255, required=True, label=_('phone'),
        error_messages={'required': _('please input phone')})
    password = forms.CharField(
        max_length=255, required=True, widget=forms.PasswordInput,
        label=_('password'),
        error_messages={'required': _('please input password')})
    again_password = forms.CharField(
        max_length=255, required=True, widget=forms.PasswordInput,
        label=_('Confirm password'),
        error_messages={'required': _('please again input password')})
    identify_code = forms.CharField(
        max_length=255, required=True, label=_('identity code'),
        error_messages={'required': _('please input identity code')})

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     if username:
    #         customer_username = Register.objects.filter(username__exact=username)
    #         if username == customer_username:
    #             raise ValidationError('username has been used')
    #
    # def clean_phone(self):
    #     phone = self.cleaned_data.get('phone')
    #     if phone:
    #         if re.match(r'^\d{3}-\d{8}|\d{4}-\d{7}$|^1(3[0-9]|5[012356789]|8[0-9]|4[57]|7[68])\d{8}$', phone) == None:
    #             raise ValidationError('phone format invalid')
    #
    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     again_password = self.cleaned_data.get('again_password')
    #     if password and again_password:
    #         if password != again_password:
    #             raise ValidationError('passwords are not consistent')

# class LoginForm(forms.Form):
#     username = forms.CharField(
#         required=True,
#         label=u"用户名",
#         error_messages={'required': '请输入用户名'},
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder':u"用户名",
#             }
#         ),
#     )
#     password = forms.CharField(
#         required=True,
#         label=u"密码",
#         error_messages={'required': u'请输入密码'},
#         widget=forms.PasswordInput(
#             attrs={
#                 'placeholder':u"密码",
#             }
#         ),
#     )
#     def clean(self):
#         if not self.is_valid():
#             raise forms.ValidationError(u"用户名和密码为必填项")
#         else:
#             cleaned_data = super(LoginForm, self).clean()

# if username and password:
#             try:
#                 member=Register.objects.get(username__exact=username)
#             except Register.DoesNotExist:
#                 self._errors['username'] = self.error_class([u"用户不存在"])
#                 return
#             if member.password != password:
#                 self._errors['password'] = self.error_class([u"密码不一致"])
#         return cleaned_data