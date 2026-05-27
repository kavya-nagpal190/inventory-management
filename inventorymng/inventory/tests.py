from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from inventory.models import Product

class ProductTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('test', password='test')
        self.client.force_authenticate(user=self.user)

    def test_create_product(self):
        res = self.client.post('/api/products/', {
            'name': 'Widget', 'quantity': 100, 'price': '9.99'
        })
        self.assertEqual(res.status_code, 201)