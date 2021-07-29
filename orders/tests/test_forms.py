from django.test import SimpleTestCase

from orders.forms import *


class TestForms(SimpleTestCase):
    def test_order_create_form_has_valid_data(self):
        form = OrderCreateForm(
            data={
                "first_name": "johnny",
                "last_name": "brown",
                "email": "johny@brown.com",
                "address": "Crowded Street 11",
                "postal_code": "33-123",
                "city": "Chill City",
            }
        )
        self.assertTrue(form.is_valid())

    def test_order_create_form_has_no_data(self):
        form = OrderCreateForm(data={})

        self.assertFalse(form.is_valid())
