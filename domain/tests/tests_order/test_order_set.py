import pytest
from domain import order


ord = order.OrderNew()

def test_get_item():
    order_dict = order.OrderDict({1: ord})
    assert order_dict[1] is ord

def test_order_set_int_key():
    order_dict = order.OrderDict({1: ord})
    assert len(order_dict) == 1

def test_order_set_str_key():
    order_dict = order.OrderDict({'1': ord})
    assert len(order_dict) == 1

def test_order_set_key_error():
    with pytest.raises(order.OrderSetKeyError):
        order.OrderDict({'': order.OrderNew()})

def test_order_by_types():
    data = {
            2: order.OrderNew(),
            3: order.OrderPayed(),}
    osa = order.OrderDict(data)
    new_orders = osa.get_orders(order.OrderNew)
    assert len(new_orders) == 1
