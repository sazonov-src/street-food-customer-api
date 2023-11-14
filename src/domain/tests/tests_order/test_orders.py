import order
import pytest
import items


def test_state_ok(order_new, checkout, payment_true):
    assert isinstance(order_new.state, order.StateCustomerNew)
    assert isinstance(order_new.cart, order.CartMutable)
    order_new.mark_as_checkouted(checkout)
    assert isinstance(order_new.state, order.StateCustomerCheckout)
    assert isinstance(order_new.cart, order.CartMutable)
    order_new.mark_as_payed(payment_true)
    assert isinstance(order_new.state, order.StateCustomerPayed)
    assert isinstance(order_new.cart, order.CartNotNutable)


def test_state_empty_cart(order_new_with_empty_cart, checkout, item, payment_true):
    assert isinstance(order_new_with_empty_cart.state, order.StateCustomerNew)
    assert isinstance(order_new_with_empty_cart.cart, order.CartMutable)
    with pytest.raises(order.OrderValueException):
        order_new_with_empty_cart.mark_as_checkouted(checkout)
    order_new_with_empty_cart.cart[item] = 1
    order_new_with_empty_cart.mark_as_checkouted(checkout)
    del order_new_with_empty_cart.cart[item]
    with pytest.raises(order.OrderValueException):
        order_new_with_empty_cart.mark_as_payed(payment_true)


def test_new_state(order_new, checkout, payment_true):
    assert isinstance(order_new.state, order.StateCustomerNew)
    with pytest.raises(order.OrderValueException):
        order_new.user_data
    with pytest.raises(order.OrderStateException):
        order_new.mark_as_payed(payment_true)
    order_new.mark_as_checkouted(checkout)
    assert isinstance(order_new.state, order.StateCustomerCheckout)
    

def test_checkout_state(order_checkouted, checkout, payment_true, payment_false):
    assert isinstance(order_checkouted.state, order.StateCustomerCheckout)
    with pytest.raises(order.OrderStateException):
        order_checkouted.mark_as_checkouted(checkout)
    with pytest.raises(order.OrderStateException):
        order_checkouted.mark_as_payed(payment_false)
    order_checkouted.mark_as_payed(payment_true)
    assert isinstance(order_checkouted.state, order.StateCustomerPayed)
    

def test_payment_state(order_payed, checkout, payment_true):
    assert isinstance(order_payed.state, order.StateCustomerPayed)
    with pytest.raises(order.OrderStateException):
        order_payed.mark_as_checkouted(checkout)
    with pytest.raises(order.OrderStateException):
        order_payed.mark_as_payed(payment_true)

