from django.test import TestCase

from models import UrlMapping

class CreateTest(TestCase):
    def test_get_create(self):
        """make sure the root page displays correctly"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        """posting to the creation page makes a shortened url"""
        response = self.client.post('/', {'url': 'http://example.com/'})
        
        um = UrlMapping.objects.get(url='http://example.com/')
        self.assertEqual(um.sha_hash, u'9c17e047f58f9220a7008d4f18152fee4d111d14')
