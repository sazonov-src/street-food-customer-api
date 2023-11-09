import order

checkout = order.UserData("Vasia", "01")

def test_checkout_state_ok():
    ord = order.OrderCheckout([],) 
    ord.to_checkout(checkout)
    assert isinstance(ord._state, order.StateCheckoutOrder)

def test_new_state_ok():
    ord = order.OrderCheckout([],) 
    assert isinstance(ord._state, order.StateNewOrder)


