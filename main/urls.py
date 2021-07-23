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

from blog.sitemaps import PostSitemap
from main.settings import MEDIA_URL, MEDIA_ROOT, DEBUG

sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls", namespace="blog")),
    path("account/", include("account.urls", namespace="account")),
    path("shop/", include("shop.urls", namespace="shop")),
    path("social-auth/", include("social_django.urls", namespace="social")),
    path("cart/", include("cart.urls", namespace="cart")),
    path("orders/", include("orders.urls", namespace="orders")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
