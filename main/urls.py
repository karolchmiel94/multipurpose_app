"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, sitemaps
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns

from blog.sitemaps import PostSitemap
from main.settings import MEDIA_URL, MEDIA_ROOT, DEBUG

from . import views

sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = i18n_patterns(
    path(_("admin/"), admin.site.urls),
    path("rosetta/", include("rosetta.urls")),
    path(_("blog/"), include("blog.urls", namespace="blog")),
    path(_("account/"), include("account.urls", namespace="account")),
    path(_("shop/"), include("shop.urls", namespace="shop")),
    path(_("social-auth/"), include("social_django.urls", namespace="social")),
    path(_("cart/"), include("cart.urls", namespace="cart")),
    path(_("orders/"), include("orders.urls", namespace="orders")),
    path(_("payments/"), include("payments.urls", namespace="payments")),
    path(_("coupons/"), include("coupons.urls", namespace="coupons")),
    path(
        "language/change/<str:language_code>/",
        views.change_language,
        name="change_language",
    ),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
)

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
