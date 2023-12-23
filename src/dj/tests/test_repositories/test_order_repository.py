import pytest

from app_order.models import CartLine
from domain.order.orders import NotFoundException

@pytest.mark.django_db
def test_add_item(domain_item, fake_repo):
    assert len(fake_repo.model.cartline_set.all()) == 0
    assert len(fake_repo.get().cart) == 0
    domain = fake_repo.get()
    domain.cart[domain_item] = 1
    fake_repo.add(domain)
    assert len(fake_repo.model.cartline_set.all()) == 1
    assert len(fake_repo.get().cart) == 1

@pytest.mark.django_db
def test_get_item(domain_item, model_item, fake_repo):
    CartLine.objects.create(order=fake_repo.model, menu_item=model_item, count=11)
    assert len(fake_repo.model.cartline_set.all()) == 1
    assert len(fake_repo.get().cart) == 1
    domain = fake_repo.get()
    del domain.cart[domain_item]
    fake_repo.add(domain)
    assert len(fake_repo.model.cartline_set.all()) == 0
    assert len(fake_repo.get().cart) == 0
    
@pytest.mark.django_db
def test_user_data(domain_user_data, domain_order, fake_repo):
    with pytest.raises(NotFoundException):
        fake_repo.get().user_data
    domain_order.mark_as_checkouted(domain_user_data)
    fake_repo.add(domain_order)
    assert fake_repo.get().user_data == domain_user_data
