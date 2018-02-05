from django.test import TestCase # noqa
from django.core.urlresolvers import reverse

import pytest


# Create your tests here.
class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('posts')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


@pytest.mark.django_db
def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
