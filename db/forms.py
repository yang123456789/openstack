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

    def clean(self):
        username = self.cleaned_data.get('username')
        if username:
            customer_username = Register.objects.filter(username=username)
            if customer_username > 1:
                raise ValidationError(_('username has been used'))
        phones = self.cleaned_data.get('phone')
        if phones:
            if re.match(r'^\d{3}-\d{8}|\d{4}-\d{7}$|^1(3[0-9]|5[012356789]|8[0-9]|4[57]|7[68])\d{8}$', phones) == None:
                raise ValidationError(_('phone format invalid'))
        passwords = self.cleaned_data.get('password')
        again_passwords = self.cleaned_data.get('again_password')
        if passwords and again_passwords:
            if passwords != again_passwords:
                raise ValidationError(_('passwords are not consistent'))