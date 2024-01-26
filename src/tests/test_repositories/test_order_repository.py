import pytest
from rest_framework.exceptions import NotFound
from app_order.repository import NewOrderRepository, create_new_order_obj
from app_order.models import Order

import domain


@pytest.mark.django_db
def test_get_new_order(user, cartlines, contact):
    repo = NewOrderRepository(user)
    with pytest.raises(NotFound):
        order_handler = repo.get()

@pytest.mark.django_db
def test_create_new_order(user, cartlines, contact):
    repo = NewOrderRepository(user)
    neworder_state = create_new_order_obj(user)
    repo.add(neworder_state)
    assert len(Order.objects.all()) == 1

@pytest.mark.django_db
def test_get_new_order_with_empty_cart(user, contact):
    repo = NewOrderRepository(user)
    with pytest.raises(domain.ErrorNewOrderState):
        create_new_order_obj(user)

@pytest.mark.django_db
def test_add_new_order_without_contact(user, cartlines):
    repo = NewOrderRepository(user)
    with pytest.raises(NotFound):
        order = repo.get().order

@pytest.mark.django_db
def test_add_new_order_with_existing_model(user, cartlines, contact):
    repo = NewOrderRepository(user)
    neworder_state = create_new_order_obj(user)
    repo.add(neworder_state)
    assert len(Order.objects.all()) == 1
    repo = NewOrderRepository(user)
    repo.add(repo.get())
    assert len(Order.objects.all()) == 1
