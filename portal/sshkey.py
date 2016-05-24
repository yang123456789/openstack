import base64
import hashlib
import uuid

def validation(ssh_public_key):
    key = base64.urlsafe_b64encode(ssh_public_key.strip().encode('ascii'))
    plain = hashlib.md5(key).hexdigest()
    return