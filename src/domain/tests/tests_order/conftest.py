import pytest
import order

import items

@pytest.fixture
def item():
    return items.Item("Some item", "Good item", 20.0)

@pytest.fixture
def item2():
    return items.Item("Some item2", "Good item", 20.0)

@pytest.fixture
def line_item(item):
    return order.OrderLine(item, order.Count(1))

@pytest.fixture
def line_item2(item2):
    return order.OrderLine(item2, order.Count(1))
