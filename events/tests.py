from django.test import TestCase
from django.urls import reverse


class EventListTests(TestCase):
    def test_index_status_code(self):
        url = reverse('events:list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
