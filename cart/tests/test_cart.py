from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sessions.middleware import SessionMiddleware
from django.http import HttpRequest, request
from django.test import Client, TestCase
from django.test.client import RequestFactory
from django.urls import reverse

from cart.cart import Cart
from main.settings import CART_SESSION_ID
from shop.models import Category, Product


class TestCart(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.factory = RequestFactory()

    def setUp(self):
        self.request = self.factory.get("/")
        middleware = SessionMiddleware()
        middleware.process_request(self.request)
        self.request.session.save()
        self.cart = Cart(self.request)

    def test_cart_being_created(self):
        self.assertTrue(self.cart is not None)

    def test_add_product_to_cart(self):
        category = Category.objects.create(name="test")
        product = Product.objects.create(
            name="test product", category=category, price=10
        )
        self.cart.add(product=product)
        self.assertEquals(len(self.cart), 1)

    def test_add_invalid_product_to_cart(self):
        category = Category.objects.create(name="test")
        product = Product.objects.create(
            name="test product", category=category, price=10
        )
        self.cart.add(product=category)
        self.assertEquals(len(self.cart), 0)

    def test_remove_product_from_cart(self):
        category = Category.objects.create(name="test")
        product = Product.objects.create(
            name="test product", category=category, price=10
        )
        self.cart.add(product=product)
        self.cart.remove(product=product)
        self.assertEquals(len(self.cart), 0)

    def test_get_total_price(self):
        category = Category.objects.create(name="test")
        product = Product.objects.create(
            name="test product", category=category, price=10
        )
        self.cart.add(product=product)
        self.assertEquals(self.cart.get_total_price(), 10)

    def test_cart_clear(self):
        self.cart.clear()
        self.assertEquals(self.request.session.get(settings.CART_SESSION_ID), None)
