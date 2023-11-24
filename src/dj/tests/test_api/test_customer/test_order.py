import pytest
from rest_framework.views import status
from rest_framework.test import APIClient

client = APIClient()

def test_get_order():
    r: Response = client.get("/api/v1/customer/new-order/")
    assert r.status_code == status.HTTP_200_OK

def test_get_cart():
    r: Response = client.get("/api/v1/customer/new-order/cart/")
    assert r.status_code == status.HTTP_200_OK

def test_get_cart_items():
    r: Response = client.get("/api/v1/customer/new-order/cart/items/")
    assert r.status_code == status.HTTP_200_OK

def test_get_cart_item_1():
    r: Response = client.get("/api/v1/customer/new-order/cart/items/1/")
    assert r.status_code == status.HTTP_200_OK

def test_post_cart_item_1():
    r: Response = client.post("/api/v1/customer/new-order/cart/items/")
    assert r.status_code == status.HTTP_200_OK

def test_put_cart_item_1():
    r: Response = client.put("/api/v1/customer/new-order/cart/items/1/")
    assert r.status_code == status.HTTP_200_OK

def test_delete_cart_item_1():
    r: Response = client.delete("/api/v1/customer/new-order/cart/items/1/")
    assert r.status_code == status.HTTP_200_OK

