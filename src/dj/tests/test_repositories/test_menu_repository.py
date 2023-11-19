import pytest
from app_menu.models import MenuItem
from dj.app_menu.repository import RepositoryMenuItem
from domain.items import Item
from mixer.backend.django import mixer


@pytest.fixture
def menu_item_model():
        return mixer.blend('app_menu.MenuItem', price=20.00)

@pytest.fixture
def menu_item_repository(menu_item_model):
        return RepositoryMenuItem(menu_item_model)


@pytest.mark.django_db
def test_repo_menuitem_get(menu_item_model, menu_item_repository):
    domain_obj = menu_item_repository.get()
    assert domain_obj.title == menu_item_model.title
    assert domain_obj.price == menu_item_model.price
    assert domain_obj.description == menu_item_model.description
    

@pytest.mark.django_db
def test_repo_menuitem_set(menu_item_repository):
    domain_obj = Item(title="some", description="some desc", price=30.00)
    menu_item_repository.add(domain_obj)
    item = MenuItem.objects.get(pk=menu_item_repository.model.pk)
    assert item.title == "some"
    assert item.description == "some desc"
    assert item.price == 30.00
