from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy

from .models import Post


class LatestPostsFeed(Feed):
    title = "My blog"
    link = reverse_lazy("blog:post_feed")
    description = "New posts of my blog."

    def items(self):
        return Post.published.all()

    def item_title(self, item: Post) -> str:
        return item.title

    def item_description(self, item: Post) -> str:
        return truncatewords(item.body, 30)
