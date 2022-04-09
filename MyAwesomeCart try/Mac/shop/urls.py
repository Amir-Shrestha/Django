from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shopindex'),
    path('about', views.about_us, name='about_us'),
    path('contact', views.contact_us, name='contact_us'),
    path('tracker', views.tracker, name='tracker'),
    path('product/<int:pro_id>', views.product_view, name='product_view'),
    path('checkout', views.checkout, name='check_out'),
    path('search', views.search, name='search'),
    path('khalti/', views.Khalti.as_view, name='khaltirequest'),
]



