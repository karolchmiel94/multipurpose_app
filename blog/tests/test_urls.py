from django.test import SimpleTestCase
from django.urls import reverse
from django.urls.base import resolve
from blog import views


class TestUrls(SimpleTestCase):
    def test_post_list_url_is_resolved(self):
        url = reverse("blog:post_list")
        self.assertEquals(resolve(url).func, views.post_list)

    def test_post_share_url_is_resolved(self):
        url = reverse("blog:post_share", kwargs={"post_id": 1})
        self.assertEquals(resolve(url).func, views.post_share)

    def test_post_search_url_is_resolved(self):
        url = reverse("blog:post_search")
        self.assertEquals(resolve(url).func, views.post_search)

    def test_post_detail_url_is_resolved(self):
        url = reverse("blog:post_detail", kwargs={"slug": "test-slug"})
        self.assertEquals(resolve(url).func, views.post_detail)
