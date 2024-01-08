#pyttest conftest.py
import pytest
from mixer.backend.django import mixer

from app_payment_callbacks import utils


@pytest.fixture
def callback_data():
    return {
    "status"         : "success",
    "amount"         : "100",
    "currency"       : "USD",
    "description"    : "description text",
    "order_id"       : "3",
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

@pytest.fixture
def data_with_bed_signature(callback_data, bed_signature):
    encoded_callback_data = utils.get_hash_data(callback_data)
    return {
        'data': encoded_callback_data,
        'signature': bed_signature,}

@pytest.fixture
def order():
    return mixer.blend("app_order.Order", id=3)

@pytest.fixture
def another_order():
    return mixer.blend("app_order.Order", id=4)
