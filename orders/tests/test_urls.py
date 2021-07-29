from django.test import SimpleTestCase
from django.urls import reverse
from django.urls.base import resolve

from orders import views


class TestUrls(SimpleTestCase):
    def test_order_create_url_is_resolved(self):
        url = reverse("orders:create_order")
        self.assertEquals(resolve(url).func, views.create_order)

    def test_admin_order_detail_url_is_resolved(self):
        url = reverse("orders:admin_order_detail", kwargs={"order_id": 1})
        self.assertEquals(resolve(url).func, views.admin_order_detail)

    def test_admin_order_pdf_url_is_resolved(self):
        url = reverse("orders:admin_order_pdf", kwargs={"order_id": 1})
        self.assertEquals(resolve(url).func, views.admin_order_pdf)
