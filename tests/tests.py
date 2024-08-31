# myapp/tests/test_api.py
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from myapp.models import MyModel

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_create(api_client):
    url = reverse('mymodel-list')
    data = {'field1': 'value1', 'field2': 'value2'}
    response = api_client.post(url, data, format='json')
    assert response.status_code == 201
    assert MyModel.objects.count() == 1

@pytest.mark.django_db
def test_read(api_client):
    obj = MyModel.objects.create(field1='value1', field2='value2')
    url = reverse('mymodel-detail', args=[obj.id])
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data['field1'] == 'value1'

@pytest.mark.django_db
def test_update(api_client):
    obj = MyModel.objects.create(field1='value1', field2='value2')
    url = reverse('mymodel-detail', args=[obj.id])
    data = {'field1': 'new_value'}
    response = api_client.patch(url, data, format='json')
    assert response.status_code == 200
    obj.refresh_from_db()
    assert obj.field1 == 'new_value'
