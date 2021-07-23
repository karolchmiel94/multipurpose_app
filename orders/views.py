from orders.tasks import order_created
from django.contrib import messages
from django.shortcuts import render

from cart.cart import Cart
from orders.forms import OrderCreateForm
from .models import OrderItem


def create_order(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item.get("product"),
                    price=item.get("price"),
                    quantity=item.get("quantity"),
                )
            cart.clear()
            messages.success(request, "Order has been placed.")
            order_created.delay(order.id)
            return render(request, "orders/order/created.html", {"order": order})
    else:
        form = OrderCreateForm()
    return render(request, "orders/order/create.html", {"cart": cart, "form": form})
