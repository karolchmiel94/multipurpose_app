from django.core.mail import send_mail

from main.celery import app

from .models import Order


@app.task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f"Order nr. {order.id}"
    message = f"You have successfully placed an order. Your order ID is {order.id}"
    mail_sent = send_mail(subject, message, "admin@myshop.com", [order.email])
    return mail_sent
