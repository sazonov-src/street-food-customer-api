import pytest

from app_order.repository import RepositoryOrder

@pytest.mark.django_db
def test_(order_model, order_domain, user_data):
    print(order_model.cartline_set.first().menu_item.title)
    repo = RepositoryOrder(order_model)
    print(repo.get())
    repo.add(order_domain)
    order_domain.mark_as_checkouted(user_data)
    repo.add(order_domain)
    print(repo.get())

    


