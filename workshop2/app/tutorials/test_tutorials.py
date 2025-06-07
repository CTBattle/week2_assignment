import pytest
from rest_framework.test import APIClient
from django.urls import reverse

@pytest.mark.django_db
def test_create_tutorial():
    client = APIClient()
    url = reverse('tutorials-list')
    data = {
        "title": "Pytest Sample",
        "description": "Testing POST endpoint.",
        "tutorial_url": "http://example.com",
        "published": True
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 201

