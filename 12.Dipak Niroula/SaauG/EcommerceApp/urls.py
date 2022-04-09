from django.urls import path
from . views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('about/', AboutView.as_view(), name="about"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('all_categories/', All_Categories.as_view(), name="all_categories"),
    path('a_product/<slug:url_slug>/', Product_view.as_view(), name="a_product"),

    path('add_to_cart/<int:pro_id>/', Add_To_Cart.as_view(), name="add_to_cart"),
    path('my_cart/', My_Cart.as_view(), name="my_cart"),
    path('manage_my_cart/<int:cartproduct_id>', Manage_My_Cart.as_view(), name="manage_my_cart"),
    path('clear_cart/', Clear_Cart.as_view(), name="clear_cart"),
    path('checkout/', Checkout.as_view(), name="checkout"),
    path('make_order/', make_order, name="make_order"),

    path('customer_register/', CustomerRegister.as_view(), name="customer_register"),
    path('log_out/', LogOut.as_view(), name="log_out"),
    path('log_in/', LogIn.as_view(), name="log_in"),

    path('customer_profile/', CustomerProfile.as_view(), name="customer_profile"),
    # path('customer_order_detial/<int:order_id>', CustomerOrderDetial.as_view(), name="customer_order_detial"),
    #Generic detail view CustomerOrderDetial must be called with either an object pk or a slug in the URLconf.
    path('customer_order_detial-<int:pk>', CustomerOrderDetial.as_view(), name="customer_order_detial"),

    path('admin_login/', AdminLogIn.as_view(), name="admin_login"),
    path('admin_dashboard/', AdminDashboard.as_view(), name="admin_dashboard"),
    path('admin_order_detial/<int:pk>', AdminOrderDetial.as_view(), name="admin_order_detial"),
    path('admin_all_orders/', AdminAllOrders.as_view(), name="admin_all_orders"),
    path('admin_order-<int:pk>-manage/', AdminOrderManage.as_view(), name="admin_order_manage"),

    path('search_product/', SearchProduct.as_view(), name="search_product"),

    #khalti payment_gateway
    path('khalti_request/', KhaltiRequest.as_view(), name="khalti_request"), #initiate payment from clieant to merchant
    path('khalti_verify/', KhaltiVerify.as_view(), name="khalti_verify"), #verify if payment is successfull with by sending token to khalti url

    #esewa payment_gateway
    path('esewa_request/', EsewaRequest.as_view(), name="esewa_request"), #initiate payment from clieant to merchant
    path('esewa_verify/', EsewaVerify.as_view(), name="esewa_verify"), #verify if payment is successfull with by sending token to khalti url

]