from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^health$", views.health_view, name="health"),
    url(r"^shopify/get_products$", views.shopify_get_products_view, name="shopify_get_products"),
]