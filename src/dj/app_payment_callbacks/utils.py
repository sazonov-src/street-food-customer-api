import base64
import hashlib
import settings
import json

def hash_data_to_sign(data: str):
    str_ = settings.LIQPAY_PRIVATE_KEY + data + settings.LIQPAY_PRIVATE_KEY
    return base64.b64encode(hashlib.sha1(str_.encode('utf-8')).digest()).decode('utf-8')

def decode_data(data: str) -> dict:
    return json.loads(base64.b64decode(data).decode('utf-8'))

def get_hash_data(data: dict):
    callback_data = json.dumps(data)
    return base64.b64encode(str(callback_data).encode('utf-8')).decode('utf-8')

def def_get_valid_data(data: str, sign: str) -> dict:
    if hash_data_to_sign(data) == sign:
        return decode_data(data)
    raise ValueError('Data is invalid')
