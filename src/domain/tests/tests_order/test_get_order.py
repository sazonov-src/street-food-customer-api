import pytest
from domain import order 

def test_get_order_not_data():
    order_data = order.ManageStatusOrder()
    obj = order_data.get_order()
    assert isinstance(obj, order.OrderNew)

def test_get_order_new(order_line):
    order_data = order.ManageStatusOrder([order_line])
    obj = order_data.get_order()
    assert isinstance(obj, order.OrderNew)

def test_get_order_checkout(order_line, user_data):
    order_data = order.ManageStatusOrder([order_line], user_data)
    obj = order_data.get_order()
    assert isinstance(obj, order.OrderCheckout)

def test_get_order_payed(order_line, user_data):
    order_data = order.ManageStatusOrder([order_line], user_data, payed=True)
    obj = order_data.get_order()
    assert isinstance(obj, order.OrderPayed)

def test_get_order_error(order_line):
    with pytest.raises(order.OrderDataError):
        order.ManageStatusOrder([order_line], payed=True)

def test_change_order_data_ok(order_line, user_data):
    order_data = order.ManageStatusOrder([order_line])
    order_data.user_data = user_data

def test_change_order_data_error(order_line):
    order_data = order.ManageStatusOrder([order_line])
    with pytest.raises(order.OrderDataError):
        order_data.payed = True
    with pytest.raises(order.OrderDataError):
        order_data.ready = True
    with pytest.raises(order.OrderDataError):
        order_data.done = True
