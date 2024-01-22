import pytest


@pytest.mark.django_db
def test_cart_get_new(client):
    res = client.get('/api/v1/customer/cart/')
    assert res.status_code == 200
    assert len(res.data['lines']) == 0
    print(res.data)

@pytest.mark.django_db
def test_cart_get(client, cart_lines1_2_3):
    res = client.get('/api/v1/customer/cart/')
    assert res.status_code == 200
    assert len(res.data['lines']) == 3

@pytest.mark.django_db
def test_cart_add(client, cart_lines1_2_3, menu_item4):
    res = client.post('/api/v1/customer/cart/', data={'menu_item': 4, 'quantity': 1})
    assert res.status_code == 200
    assert len(res.data['lines']) == 4
    res = client.get('/api/v1/customer/cart/')
    assert len(res.data['lines']) == 4

@pytest.mark.django_db
def test_cart_add_that_in_cart(client, cart_lines1_2_3):
    res = client.post('/api/v1/customer/cart/', data={'menu_item': 3, 'quantity': 1})
    assert res.status_code == 200
    assert len(res.data['lines']) == 3
    res = client.get('/api/v1/customer/cart/')
    assert len(res.data['lines']) == 3

@pytest.mark.django_db
def test_cart_remove(client, cart_lines1_2_3):
    res = client.delete('/api/v1/customer/cart/3/')
    assert res.status_code == 200
    res = client.get('/api/v1/customer/cart/')
    assert len(res.data['lines']) == 2

@pytest.mark.django_db
def test_cart_plus(client, cart_lines1_2_3):
    res = client.post('/api/v1/customer/cart/1/plus_quantity/')
    assert res.status_code == 200
    assert res.data['quantity'] == 2
    res = client.post('/api/v1/customer/cart/1/minus_quantity/')
    assert res.status_code == 200
    assert res.data['quantity'] == 1

@pytest.mark.django_db
def test_cart_minus(client, cart_lines1_2_3):
    res = client.post('/api/v1/customer/cart/1/minus_quantity/')
    assert res.status_code == 400
