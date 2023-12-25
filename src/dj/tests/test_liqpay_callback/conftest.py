#pyttest conftest.py
import pytest

from app_payment_callbacks import utils


@pytest.fixture
def callback_data():
    return {
    "action"         : "pay",
    "amount"         : "1",
    "currency"       : "USD",
    "description"    : "description text",
    "order_id"       : "order_id_1",
    "version"        : "3"}

@pytest.fixture
def bed_signature():
    return "111"

@pytest.fixture
def data(callback_data):
    encoded_callback_data = utils.get_hash_data(callback_data)
    return {
        'data': encoded_callback_data,
        'signature': utils.hash_data_to_sign(encoded_callback_data),}
