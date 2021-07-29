from django.test import TestCase, Client
from django.urls import reverse

import json

from blog.models import *


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse("blog:post_list")
        self.detail_url = reverse("blog:post_detail", args=["test-post"])
        self.user = User.objects.create_user(username="testuser", password="12345")
        login = self.client.login(username="testuser", password="12345")

        self.post1 = Post.objects.create(title="Test post", author=self.user)

    def test_post_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post/list.html")

    def test_post_detail_GET(self):
        response = self.client.get(self.detail_url)
        print(self.detail_url)
        print(self.post1.slug)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post/detail.html")
