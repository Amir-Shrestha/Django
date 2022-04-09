from django.urls import path
from . import views

urlpatterns = [
    path("", views.shop, name="shop"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("tracker/", views.tracker, name="tracker"),
    path("search/", views.search, name="search"),
    path("product_view/", views.product_view, name="product_view"),
    path("checkout/", views.checkout, name="checkout"),
]
