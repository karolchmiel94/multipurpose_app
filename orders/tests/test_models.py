from django.test import TestCase
from django.test.client import Client

from orders.models import *


class TestModels(TestCase):
    def setUp(self):
        self.client = Client()
