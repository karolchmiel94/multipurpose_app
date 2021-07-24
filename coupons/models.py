from statistics import mode

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Coupon(models.Model):
    code = models.CharField(max_length=255, unique=True)
    discount = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(0)]
    )
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    is_active = models.BooleanField()

    def __str__(self) -> str:
        return self.code
