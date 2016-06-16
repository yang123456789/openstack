from db.views import *
import base64
import hashlib
import hmac
import uuid


def validation(ssh_public_key):
    try:
        key = base64.urlsafe_b64encode(ssh_public_key.strip())
        plain = hashlib.md5(key).hexdigest().upper()
        return plain
    except Exception:
        return False


def generation_two_keys(app_key, secret_key):
    app_key = utf8(app_key)
    secret_key = utf8(secret_key)
    app_key = hmac.new(app_key).digest()
    secret_key = hmac.new(secret_key).digest()[0:10].upper()
    secret_key = secret_key + hmac.new(secret_key).digest()[10:]
    ssh_public_key = app_key + secret_key
    return ssh_public_key