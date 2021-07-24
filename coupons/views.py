from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from .forms import CouponApplyForm
from .models import Coupon


@require_POST
def apply_coupon(request):
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data.get("code")
        try:
            coupon = Coupon.objects.get(
                code__iexact=code,
                valid_from__lte=now,
                valid_to__gte=now,
                is_active=True,
            )
            request.session["coupon_id"] = coupon.id
        except Coupon.DoesNotExist:
            request.session["coupon_id"] = None
    return redirect("cart:cart_detail")