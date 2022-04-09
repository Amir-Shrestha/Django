from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('register_user', views.register_user, name='register_user'),
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),

    path('', views.dashboard, name='dashboard'),
    path('products/', views.products, name='products'),
    path('customer_detial/<str:c_id>', views.customer_detial, name='customer_detial'),
    path('order_product/<str:c_id>', views.order_product, name='order_product'),
    path('update_order/<str:c_id>', views.update_order, name='update_order'),
    path('delete_order/<str:o_id>', views.delete_order, name='delete_order'),

    path('customer_dashboard', views.customer_dashboard, name='customer_dashboard'),
    path('profile_settings', views.profile_settings, name='profile_settings'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="Accounts/reset_password.html"), name="reset_password"), #ClassBaseView_Reset_Form
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="Accounts/reset_password_form_sent_message.html"), name="password_reset_done"), #ClassBaseView_RestForm_send_in_email_Message
    path('reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="Accounts/reset_password_form.html"), name="password_reset_confirm"), #ClassBaseView_Reset_Conformation_Form_We_See_In_Our_Email
    path('reset_password_success/', auth_views.PasswordResetCompleteView.as_view(template_name="Accounts/reset_password_success.html"), name="password_reset_complete"), #ClassBaseView_Reset_Success_Message

]
