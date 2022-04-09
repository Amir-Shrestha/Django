from django.shortcuts import render, HttpResponse, redirect
from . models import Product, Profile, Order
from .forms import OrderForm
from django.forms import inlineformset_factory
from .filters import OrderFilter
from .forms import RegisterForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group

# Create your views here.

@login_required(login_url='login_user')
# @allowed_users(allowed_roles=['admin'])
@admin_only
def dashboard(request):
    customers = Profile.objects.all()
    orders = Order.objects.all()

    total_orders = orders.count()
    total_pending_orders = orders.filter(status='Pending').count()
    total_delivery_out_orders = orders.filter(status='Out for delivery').count()
    total_delivered_orders = orders.filter(status='Delivered').count()

    params = {'customers':customers, 'orders':orders, 'total_orders':total_orders, 'total_pending_orders':total_pending_orders, 'total_delivery_out_orders':total_delivery_out_orders, 'total_delivered_orders':total_delivered_orders}
    return render(request, 'accounts/dashboard.html', params)




@login_required(login_url='login_user')
@allowed_users(allowed_roles=['customer'])
def customer_dashboard(request):
    customer = request.user.profile
    orders = request.user.profile.order_set.all()
    # print(orders)

    total_orders = orders.count()
    total_pending_orders = orders.filter(status='Pending').count()
    total_delivery_out_orders = orders.filter(status='Out for delivery').count()
    total_delivered_orders = orders.filter(status='Delivered').count()

    params = {'customer':customer, 'orders':orders, 'total_orders':total_orders, 'total_pending_orders':total_pending_orders, 'total_delivery_out_orders':total_delivery_out_orders, 'total_delivered_orders':total_delivered_orders}
    return render(request, 'accounts/customer_dashboard.html', params)




@login_required(login_url='login_user')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    params = {'products':products}
    return render(request, 'accounts/products.html', params)





@login_required(login_url='login_user')
@allowed_users(allowed_roles=['admin'])
def customer_detial(request, c_id):
    customer = Profile.objects.get(id=c_id)
    orders = Order.objects.filter(profile=customer)
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    params = {'customer':customer, 'orders':orders, 'myFilter':myFilter}
    return render(request, 'accounts/customer_detial.html', params)





@login_required(login_url='login_user')
@allowed_users(allowed_roles=['admin','customer'])
def order_product(request, c_id):
    OrderFormSet_instance = inlineformset_factory(Profile, Order, fields=('product', 'status'), extra=5)
    profile = Profile.objects.get(id=c_id)
    if request.method == 'POST':
        # order_form = OrderForm(request.POST)
        orders_formset = OrderFormSet_instance(request.POST, instance=Profile)
        if orders_formset.is_valid():
            orders_formset.save()
            if request.user.is_staff:
                return redirect('dashboard')
            else:
                return redirect('customer_dashboard')

    orders_formset = OrderFormSet_instance(queryset=Order.objects.none(), instance=profile)
    # order_form = OrderForm(initial={'profile':profile})
    params = {'profile':profile, 'orders_formset':orders_formset}
    return render(request, 'accounts/order_product.html', params)





@login_required(login_url='login_user')
@allowed_users(allowed_roles=['admin'])
def update_order(request, c_id):
    order_product = Order.objects.get(id=c_id)

    if request.method == 'POST':
        order_form = OrderForm(request.POST, instance=order_product)
        if order_form.is_valid():
            order_form.save()
            return redirect('dashboard')

    order_form = OrderForm(instance=order_product)
    print(order_form)

    params = {'orders_formset':order_form}
    return render(request, 'accounts/order_product.html', params)





@login_required(login_url='login_user')
@allowed_users(allowed_roles=['admin'])
def delete_order(request, o_id):
	order = Order.objects.get(id=o_id)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'order':order}
	return render(request, 'accounts/delete.html', context)




@unauthenticated_user
def register_user(request):
    if request.method == "POST":
        user_register_form = RegisterForm(request.POST)
        if user_register_form.is_valid():
            user = user_register_form.save()
            username = user_register_form.cleaned_data.get('username')

            messages.success(request, 'Account was successfully created for ' + username)
            return redirect('login_user')
    user_register_form = RegisterForm()
    params = {'user_register_form':user_register_form}
    return render(request, 'accounts/register_user.html', params)




@unauthenticated_user
def login_user(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        upass = request.POST.get('password')
        user = authenticate(request, username=uname, password=upass)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.warning(request, 'Incorrect Username or Password !!!')
    return render(request, 'accounts/login_user.html')





@login_required(login_url='login_user')
def logout_user(request):
    logout(request)
    return redirect('login_user')



@login_required(login_url='login_user')
@allowed_users(allowed_roles=['customer'])
def profile_settings(request):
    profile_instance = request.user.profile

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile_instance)
        if profile_form.is_valid():
            profile_form.save()

    profile_form = ProfileForm(instance=profile_instance)
    params = {'profile_form':profile_form}
    return render(request, 'accounts/profile_settings.html', params)




