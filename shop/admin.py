from django.contrib import admin

from parler.admin import TranslatableAdmin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ["name", "slug"]

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ["name", "slug", "price", "is_available", "created_at", "updated_at"]
    list_filter = ["is_available", "created_at", "updated_at"]
    list_editable = ["price", "is_available"]

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("name",)}
