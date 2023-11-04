import pytest

import order

def test_new_cart(line_item, line_item2):
    ord = order.CartChangeable(line_item, line_item2)
    assert len(ord.lines) == 2
    assert ord.total_price == 50.0

def test_empty_cart():
    ord = order.CartChangeable()
    assert len(ord.lines) == 0

def test_add_line(line_item, line_item2):
    ord = order.CartChangeable(line_item)
    ord.add_line(line_item2)
    assert len(ord.lines) == 2

def test_rm_line(line_item):
    ord = order.CartChangeable(line_item)
    ord.rm_line(line_item)
    assert len(ord._lines) == 0
    
