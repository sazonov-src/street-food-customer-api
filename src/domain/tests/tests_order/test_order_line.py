import pytest

import order

def test_valid_count():
    assert order.Count(5) == 5
    assert order.Count("5") == 5

def test_invalid_count():
    with pytest.raises(ValueError):
        order.Count(0)
    with pytest.raises(ValueError):
        order.Count(-1)

def test_total_price(item):
    line = order.OrderLine(item, order.Count(5)) 
    assert line.total_price == item.price * 5

def test_minus_count(item):
    line = order.OrderLine(item, order.Count(5)) 
    line.minus_count()
    assert line.count == 4

def test_plus_count(item):
    line = order.OrderLine(item, order.Count(5)) 
    line.plus_count()
    assert line.count == 6

def test_bed_minus_count(item):
    line = order.OrderLine(item, order.Count(1)) 
    with pytest.raises(ValueError):
        line.minus_count()

def test_eq_orderline(item):
    line1 = order.OrderLine(item, order.Count(1)) 
    line2 = order.OrderLine(item, order.Count(5)) 
    assert line1 == line2
