import pytest

import items

@pytest.fixture
def item():
    return items.Item("Some item", "Good item", 20.0)
