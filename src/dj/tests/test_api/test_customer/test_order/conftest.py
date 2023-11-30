import pytest
from mixer.backend.django import mixer
from rest_framework.test import APIClient


@pytest.fixture
@pytest.mark.django_db
def user():
    return mixer.blend('auth.user')


@pytest.fixture
@pytest.mark.django_db
def client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client

