from django.utils.translation import ugettext as _


class OpenstackException(Exception):
    msg_fmt = _('OpenstackException')

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