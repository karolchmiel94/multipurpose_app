import django
from django.shortcuts import redirect
from django.utils import translation


def change_language(request, language_code="en"):
    redirect_to = request.META.get("HTTP_REFERER")
    translation.activate(language_code)
    request.session["django_language"] = language_code
    return redirect(redirect_to)
