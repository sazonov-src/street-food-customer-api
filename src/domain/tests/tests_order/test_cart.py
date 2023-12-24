
import items
import order

item = items.Item("Some item", "Good item", 20.0)
item2 = items.Item("Some item2", "Good item", 30.0)

def test_new_cart():
    cart = order.CartMutable((item, 1))
    assert len(cart) == 1
    assert cart[item] == 1
    assert item in cart
    assert item2 not in cart

def test_bad_count():
    cart = order.CartMutable((item, "1"))
    assert cart[item] == 1

def test_change_item():
    cart = order.CartMutable((item, 1))
    cart[item] += 1
    assert cart[item] == 2
    
def test_same_item():
    cart = order.CartMutable((item, 1), (item, 2))
    assert len(cart) == 1

def test_add_item():
    cart = order.CartMutable()
    cart[item] = 1
    assert len(cart) == 1

def test_rm_cart():
    cart = order.CartMutable((item , 1))
    cart.pop(item)
    assert len(cart) == 0

def test_total_price():
    cart = order.CartMutable((item, 1), (item2, 1))
    assert cart.total_price == 50
