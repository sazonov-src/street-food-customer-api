import pytest
from domein import order 

def test_get_order_not_data():
    order_data = order.OrderData()
    obj = order_data.get_order()
    assert isinstance(obj, order.OrderNew)

def test_get_order_new(order_line):
    order_data = order.OrderData([order_line])
    obj = order_data.get_order()
    assert isinstance(obj, order.OrderNew)

def test_get_order_checkout(order_line, user_data):
    order_data = order.OrderData([order_line], user_data)
    obj = order_data.get_order()
    assert isinstance(obj, order.OrderCheckout)

def test_get_order_payed(order_line, user_data):
    order_data = order.OrderData([order_line], user_data, payed=True)
    obj = order_data.get_order()
    assert isinstance(obj, order.OrderPayed)

def test_get_order_error(order_line):
    with pytest.raises(order.OrderDataError):
        order.OrderData([order_line], payed=True)
