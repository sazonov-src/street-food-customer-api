import pytest


@pytest.mark.django_db
def test_get_new_order(client, contact, cart_lines1_2_3):
    client.post('/api/v1/customer/new-order/')
    response = client.get('/api/v1/customer/new-order/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_get_empty_new_order(client, contact, cart_lines1_2_3):
    response = client.get('/api/v1/customer/new-order/')
    assert response.status_code == 404

@pytest.mark.django_db
def test_empty_cart(client, contact):
    response = client.post('/api/v1/customer/new-order/')
    assert response.status_code == 400

@pytest.mark.django_db
def test_without_contact(client, cart_lines1_2_3):
    response = client.post('/api/v1/customer/new-order/')
    assert response.status_code == 400
