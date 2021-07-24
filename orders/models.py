from decimal import Decimal

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from coupons.models import Coupon
from shop.models import Product
from utils.model_utils import TimeStampMixin


class Order(TimeStampMixin):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField()
    address = models.CharField(max_length=256)
    postal_code = models.CharField(max_length=50)
    city = models.CharField(max_length=128)
    paid = models.BooleanField(default=False)
    braintree_id = models.CharField(max_length=200, blank=True)
    coupon = models.ForeignKey(
        Coupon, blank=True, null=True, on_delete=models.CASCADE, related_name="orders"
    )
    discount = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return f"Order {self.id}"

    def get_discount(self):
        return sum(item.get_cost() for item in self.items.all()) * (
            self.discount / Decimal(100)
        )

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount / Decimal(100))


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self) -> str:
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
