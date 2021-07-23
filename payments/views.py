from os import error

import braintree
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render

from main.settings import BRAINTREE_CONF
from orders.models import Order

gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)


def payment_process(request):
    order_id = request.session.get("order_id")
    order = get_object_or_404(Order, id=order_id)

    if request.method == "POST":
        nonce = request.POST.get("payment_method_nonce", None)
        result = gateway.transaction.sale(
            {
                "amount": f"{order.get_total_cost():.2f}",
                "payment_method_nonce": nonce,
                "options": {"submit_for_settlement": True},
            }
        )
        if result.is_success:
            order.paid = True
            order.braintree_id = result.transaction.id
            order.save()
            return redirect("payments:done")
        else:
            return redirect("payments:canceled")
    else:
        # client_token = gateway.client_token.generate()
        # Braintree is scuffed and breaks while trying to generate token. I'll
        # try to implement Strpe instead later
        return render(
            request,
            "payments/process.html",
            {"order": order, "client_token": "client_token"},
        )


def payment_done(request):
    return render(request, "payments/done.html")


def payment_canceled(request):
    return render(request, "payments/canceled.html")
