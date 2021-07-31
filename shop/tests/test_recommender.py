from shop.models import Category, Product
from cart.cart import Cart
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase
from django.test.client import RequestFactory

from shop.recommender import Recommender


class TestRecommender(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = RequestFactory()

    def setUp(self):
        self.request = self.factory.get("/")
        middleware = SessionMiddleware()
        middleware.process_request(self.request)
        self.request.session.save()
        self.cart = Cart(self.request)
        self.r = Recommender()
        self.r.clear_purchases()

    def test_products_bought_together(self):
        self.r.clear_purchases()
        category = Category.objects.create(name="test")
        product = Product.objects.create(
            name="test product", category=category, price=10
        )
        product2 = Product.objects.create(
            name="test product 2", category=category, price=20
        )
        product3 = Product.objects.create(
            name="test product 3", category=category, price=19
        )
        product4 = Product.objects.create(
            name="test product 4", category=category, price=29
        )
        self.cart.add(product=product)
        self.cart.add(product=product3)
        self.cart.add(product=product4)
        self.r.products_bought([product, product3, product4])
        self.assertEquals(
            self.r.suggest_products_for([product]), [product4, product3, product2]
        )
