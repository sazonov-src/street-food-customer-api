import base64
import hashlib
import json
import domain_setup


class LiqpaySDK:
    def __init__(self, data: dict) -> None:
        self.data = data

    @property
    def signature(self):
        str_ = domain_setup.LIQPAY_PRIVATE_KEY + self.encode_data + domain_setup.LIQPAY_PRIVATE_KEY
        return base64.b64encode(hashlib.sha1(str_.encode('utf-8')).digest()).decode('utf-8')

    @staticmethod
    def decode_data(data: str) -> dict:
        return json.loads(base64.b64decode(data).decode('utf-8'))

    @property
    def encode_data(self) -> str:
        return base64.b64encode(
                    str(json.dumps(self.data)).encode('utf-8')
                ).decode('utf-8')

    def validate(self, sign: str) -> None:
        if self.signature != sign:
            raise ValueError('Data is invalid')
