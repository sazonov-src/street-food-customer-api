import order
import pytest

checkout = order.UserData("Vasia", "01")

def test_checkout_state_ok():
    ord = order.CustomerOrder([],) 
    ord.mark_as_checkout(checkout)
    assert isinstance(ord.state, order.StateCustomerCheckout)
    assert isinstance(ord.cart, order.CartMutable)
    assert isinstance(ord.user_data, order.UserData)

def test_new_state_ok():
    ord = order.CustomerOrder([],) 
    assert isinstance(ord.state, order.StateCustomerNew)
    assert isinstance(ord.cart, order.CartMutable)
    with pytest.raises(ValueError):
        ord.user_data



