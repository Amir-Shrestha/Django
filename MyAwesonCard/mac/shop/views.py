from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def shop(request):
    return render(request, "shop/shop.html")


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    return render(request, "shop/contact.html")


def tracker(request):
    return render(request, "shop/tracker.html")


def search(request):
    return render(request, "shop/search.html")


def product_view(request):
    return render(request, "shop/product_view.html")


def checkout(request):
    return render(request, "shop/checkout.html")
