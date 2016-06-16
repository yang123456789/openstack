class OpnstackException(Exception):
    msg_fmt = ('OpnstackException')

    def __init__(self, message=None):
        # message = self.msg_fmt
        # self.message = message
        if not message:
            try:
                message = self.msg_fmt
            except Exception:
                return
        self.message = message
        super(OpnstackException, self).__init__(message)

class VitityLenException(OpnstackException):
    msg_fmt = ('Register list can not more than one')

class AuthTokenVitity(OpnstackException):
    msg_fmt = ('AuthToken vititied invalid')