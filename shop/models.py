from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse

from parler.models import TranslatableModel, TranslatedFields

from utils.model_utils import TimeStampMixin


class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255, db_index=True),
        slug=models.SlugField(max_length=255, unique=True),
    )

    class Meta:
        # ordering = ("name",)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])


class Product(TimeStampMixin, TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255, db_index=True),
        slug=models.SlugField(max_length=255, db_index=True),
        description=models.TextField(blank=True),
    )
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    # class Meta:
    #     ordering = ("name",)
    #     index_together = (("id", "slug"),)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_detail", kwargs={"id": self.id, "slug": self.slug})
