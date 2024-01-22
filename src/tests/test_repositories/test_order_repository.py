import pytest
from app_order.repository import CustomNewOrderStateRepository
from app_order.models import OrderModel

import domain


@pytest.mark.django_db
def test_get_new_order(user, cartlines, contact):
    repo = CustomNewOrderStateRepository(user)
    order_handler = repo.get()
    repo.add(order_handler.order)
    assert len(OrderModel.objects.all()) == 1
    assert isinstance(order_handler, domain.StateOrderNew)

@pytest.mark.django_db
def test_get_new_order_with_empty_cart(user, contact):
    repo = CustomNewOrderStateRepository(user)
    with pytest.raises(domain.ErrorNewOrderState):
        order = repo.get().order

@pytest.mark.django_db
def test_add_new_order_without_contact(user, cartlines):
    repo = CustomNewOrderStateRepository(user)
    with pytest.raises(ValueError):
        order = repo.get().order

@pytest.mark.django_db
def test_add_new_order_with_existing_model(user, cartlines, contact):
    repo = CustomNewOrderStateRepository(user)
    repo.add(repo.get().order)
    assert len(OrderModel.objects.all()) == 1
    repo = CustomNewOrderStateRepository(user)
    repo.add(repo.get().order)
    assert len(OrderModel.objects.all()) == 1
