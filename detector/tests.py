from django.urls import reverse, resolve
from django.test import TestCase

from . import views


class HomeTests(TestCase):
    def test_index_status_code(self):
        url = reverse('detector:index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_index_url_resolves_index_view(self):
        view = resolve('/')
        self.assertEquals(view.func, views.index)