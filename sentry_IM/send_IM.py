# encoding: utf-8
"""大象客户端库"""

import json
import requests
import requests_APISign


class IM():
    def __init__(self, fromName, fromUid, client_id, client_secret, toAppId=1):
        self.fromName = fromName
        self.fromUid = fromUid
        self.toAppId = toAppId

        self.client_id = client_id
        self.client_secret = client_secret
        self.MWS = requests_APISign.APISign(self.client_id, self.client_secret)

    def send_to(self, receivers={}, message=None):
        """receivers为发送目标的列表，注意是列表！！！
        message目前默认为文本型；其它类型回头再说吧"""

        if not receivers or not message:
            return

        data = dict()
        data['fromName'] = self.fromName
        data['fromUid'] = self.fromUid
        data['toAppid'] = self.toAppId

        data['receivers'] = receivers

        data['messageType'] = 'text'
        data['body'] = {"text": message}

        r = requests.put('网址隐藏了',
                         auth=self.APISign,
                         headers={"Content-Type":
                                  "application/json;charset=utf-8"},
                         data=json.dumps(data))
        return (r.status_code, r.text)
