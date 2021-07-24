from coupons.forms import CouponApplyForm
from cart.forms import CartAddProductForm
from shop.models import Product
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .cart import Cart
from shop.models import Product


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item["update_quantity_form"] = CartAddProductForm(
            initial={"quantity": item.get("quantity"), "override": True}
        )
        coupon_apply_form = CouponApplyForm()
    return render(
        request,
        "cart/detail.html",
        {"cart": cart, "coupon_apply_form": coupon_apply_form},
    )


@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd.get("quantity"),
            override_quantity=cd.get("override"),
        )
    return redirect("cart:cart_detail")


@require_POST
def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("cart:cart_detail")
