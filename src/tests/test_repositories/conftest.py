import pytest
from mixer.backend.django import mixer
from domain.models import cart

@pytest.fixture
def user():
    return mixer.blend('auth.User')

@pytest.fixture
def cartlines(user):
    return [mixer.blend(
        'app_cart.CartLine', 
        menu_item=item, 
        user=user) 
     for item in mixer.cycle(3).blend('app_menu.MenuItem')]
        
@pytest.fixture
def menuitem33():
    return mixer.blend('app_menu.MenuItem', id=33, price=10)

@pytest.fixture
def menuitem33_domain(menuitem33):
    return cart.Product(id=33, price=10)

@pytest.fixture
def contact(user):
    return mixer.blend('app_contact.Contact', user=user, name='name', phone='phone')
