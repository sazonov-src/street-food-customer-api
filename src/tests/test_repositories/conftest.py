import pytest
from mixer.backend.django import mixer

import domain


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
    return domain.ModelCartItem(id=33, price=10)

@pytest.fixture
def contact(user):
    return mixer.blend('app_contact.Contact', user=user, name='name', phone='phone')

@pytest.fixture
def pay_callbacks():
    pass
