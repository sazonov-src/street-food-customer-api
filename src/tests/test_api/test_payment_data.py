import pytest


@pytest.mark.django_db
def test_payment_data(client, order):
    response = client.get('/api/v1/customer/new-order/payment-data/')
    assert response.status_code == 200
    assert type(response.data['data']) == str
    assert type(response.data['signature']) == str
    assert response.data.keys() == {'data', 'signature'}

@pytest.mark.django_db
def test_payment_data_fail(client):
    response = client.get('/api/v1/customer/new-order/payment-data/')
    assert response.status_code == 404
