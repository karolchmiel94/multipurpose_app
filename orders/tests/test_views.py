from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from orders.views import *
from shop.models import Product


# class TestViews(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create_user(username="testuser", password="12345")
#         self.cart = Cart(self.client.session)
# login = self.client.login(username="testuser", password="12345")
# product = Product.objects.create()

# def test_create_order_GET(self):
#     response = self.client.get("orders:create_order")

#     self.assertEquals(response.status_code, 200)
#     self.assertTemplateUsed(response, "orders/order/create.html")
