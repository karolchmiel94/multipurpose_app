from django.db.models.query import QuerySet
from django.test import TestCase, Client

from blog.models import *


class TestModels(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="12345")
        login = self.client.login(username="testuser", password="12345")

        self.post1 = Post.objects.create(title="Test post", author=self.user)

    def test_post_has_assigned_slug_on_creation(self):
        self.assertEquals(self.post1.slug, "test-post")
