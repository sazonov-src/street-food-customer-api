import pytest
from domein import order 

def test_get_order_not_data():
    obj = order.get_order()
    assert isinstance(obj, order.OrderNew)

def test_get_order_new(order_line):
    obj = order.get_order([order_line])
    assert isinstance(obj, order.OrderNew)

def test_get_order_checkout(order_line, user_data):
    obj = order.get_order([order_line], user_data)
    assert isinstance(obj, order.OrderCheckout)

def test_get_order_payed(order_line, user_data):
    obj = order.get_order([order_line], user_data, payed=True)
    assert isinstance(obj, order.OrderPayed)

def test_get_order_error(order_line):
    with pytest.raises(order.OrderDataError):
        order.get_order([order_line], payed=True)
