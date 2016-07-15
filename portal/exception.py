from django.utils.translation import ugettext as _


class OpenstackException(Exception):
    msg_fmt = ('OpenstackException')

    def __init__(self, message=None):
        if not message:
            try:
                message = self.msg_fmt
            except Exception:
                return
        self.message = message
        super(OpenstackException, self).__init__(message)


class VitityLenException(OpenstackException):
    msg_fmt = _('Register list can not more than One')


class AuthTokenVitity(OpenstackException):
    msg_fmt = _('AuthToken vititied invalid')


class UsernameException(OpenstackException):
    msg_fmt = _('username has been used')


class PhoneException(OpenstackException):
    msg_fmt = _('phone format invalid')


class PasswordIdentityException(OpenstackException):
    msg_fmt = _('passwords are not consistent')