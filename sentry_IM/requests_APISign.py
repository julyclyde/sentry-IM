"""WebAPI Signature

    Usage reference
    http://docs.python-requests.org/en/latest/user/authentication/#new-forms-of-authentication
"""

import email.utils
import base64
import hashlib
import hmac
import requests


class APISign(requests.auth.AuthBase):
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def __call__(self, r):
        date = email.utils.formatdate(timeval=None,
                                      localtime=False, usegmt=True)

        string_to_sign = None # 须签名的字符串格式隐藏了
        signature = None # 签名算法隐藏了

        r.headers["Date"] = date
        r.headers["Authorization"] = "header格式隐藏了"

        return r
