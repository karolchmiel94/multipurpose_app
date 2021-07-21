from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from taggit.managers import TaggableManager

from utils.model_utils import TimeStampMixin, generate_unique_slug


class StatusChoices(models.TextChoices):
    DRAFT = "draft", _("Draft")
    PUBLISHED = "published", _("Published")


class PublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super(PublishedManager, self)
            .get_queryset()
            .filter(status=StatusChoices.PUBLISHED)
        )


class Post(TimeStampMixin):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    body = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=10, choices=StatusChoices.choices, default=StatusChoices.DRAFT
    )
    tags = TaggableManager(blank=True)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ("-published_at",)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.slug])

    def get_active_comments(self):
        return self.comments.filter(is_active=True)


class Comment(TimeStampMixin):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("created_at",)

    def __str__(self) -> str:
        return f"Comment by {self.name} on {self.post}"


# mofe to signal's.py
def post_pre_save_receiver(sender, instance: Post, **kwargs):
    instance.slug = generate_unique_slug(instance, instance.title)


pre_save.connect(post_pre_save_receiver, sender=Post)
