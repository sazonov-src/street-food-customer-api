import pytest
from app_order.repository import CustomNewOrderRepository
from app_order.models import OrderModel

import domain


@pytest.mark.django_db
def test_get_new_order(user, cartlines, contact):
    repo = CustomNewOrderRepository(user)
    order_handler = repo.get()
    repo.add(order_handler.order)
    assert len(OrderModel.objects.all()) == 1
    assert isinstance(order_handler, domain.NewOrderHandler)

@pytest.mark.django_db
def test_get_new_order_with_empty_cart(user, contact):
    repo = CustomNewOrderRepository(user)
    with pytest.raises(domain.NewOrderError):
        order = repo.get().order

@pytest.mark.django_db
def test_add_new_order_without_contact(user, cartlines):
    repo = CustomNewOrderRepository(user)
    with pytest.raises(ValueError):
        order = repo.get().order

@pytest.mark.django_db
def test_add_new_order_with_existing_model(user, cartlines, contact):
    repo = CustomNewOrderRepository(user)
    repo.add(repo.get().order)
    assert len(OrderModel.objects.all()) == 1
    repo = CustomNewOrderRepository(user)
    repo.add(repo.get().order)
    assert len(OrderModel.objects.all()) == 1
