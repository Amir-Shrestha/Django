from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, CreateView, FormView, DetailView
from . models import *
from .forms import OrderForm, CustomerRegistrationForm, UserLogInForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
import requests




class EcomMixin(object): #add logged in customer to the cart.customer
    def dispatch(self, request, *args, **kwargs):
        cart_id = request.session.get("cart_id")
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
            if request.user.is_authenticated and request.user.customer:
                cart_obj.customer = request.user.customer
                cart_obj.save()
        return super().dispatch(request, *args, **kwargs)



# Create your views here.
# class HomeView(EcomMixin, TemplateView):
class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        allproducts__queryset = Product.objects.all().order_by("-id")
        paginator = Paginator(allproducts__queryset, 4) # Show 25 contacts per page.
        page_number = self.request.GET.get('page')
        page_obj_with_4_products_obj = paginator.get_page(page_number)
        context['page_obj_with_4_products_obj'] = page_obj_with_4_products_obj #create object of Product class with Pagination as page_obj_with_4_products_obj and pass to template as item of context list
        # print(type(context))
        return context


class All_Categories(EcomMixin, TemplateView):
    template_name = "all_categories.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all() #create object of Category class as categories and pass to template as item of context list
        return context


class Product_view(EcomMixin, TemplateView):
    template_name = "a_product_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_slug = self.kwargs['url_slug']
        product_obj = Product.objects.get(slug=product_slug) # get unique object with requested slug value
        # print(product)
        context['product_obj'] = product_obj

        product_obj.view_count += 1
        product_obj.save()

        return context



class Add_To_Cart(EcomMixin, TemplateView):
    template_name = "add_to_cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context) # it already contain view key with vale
        # print(type(context))
        # print(type(kwargs)) # so product_id =  self.kwargs['pro_id']

        # 1.get product id from requested url
        product_id =  self.kwargs['pro_id']
        # print(product_id)
        # print(type(product_id))
        # 2.then get product corresponding to product_id from requested url
        product_obj = Product.objects.get(id=product_id)

        # 3.then check if cart exist in database or not? For this we use session
        cart_id = self.request.session.get("cart_id", None) #if cart_id session_varaible is present in our session then return the value of cart_id session_varaible else return None
        if cart_id: # this runs once you have already click add to cart button & cart object is created and fetech that cart object from database
            cart_obj = Cart.objects.get(id=cart_id) #3.5 if cart/cart_object with id(cart_id) exist in database model class table you need to get/fetech that cart
            print("you have a cart with cart_id ",cart_obj.id)

            # 4.then check if product already exist in cart
                # item already exists in cart
            selected_product_in_cart = cart_obj.cartproduct_set.filter(product=product_obj) #4.1 QureySet with only one object #3.6 get the seleceted art to cart product reverse relationship #One Cart can have relation withn many CartProduct
            if selected_product_in_cart.exists(): # 4.4 if selected_product  from art_to_cart button is already present in cart more like in (CartProduct class) then just edit some of attributes of selected_product object(i.e : cartproduct = selected_product_in_cart.last())
                print(selected_product_in_cart)
                cartproduct = selected_product_in_cart.last() # 4.5 Last object of QuerySet
                print(cartproduct)
                cartproduct.quantity += 1
                cartproduct.sub_total += product_obj.selling_price
                cartproduct.save()
                cart_obj.total_amount += product_obj.selling_price #Total Amount of cart : Sum of total amount of all product in cart
                cart_obj.save()
                    # new item is added in cart
            else:# 4.1 if selected_product  from art_to_cart button is not present in cart more like in (CartProduct class), Create an new object of CartProduct class with all needed attributes and save it into database table
                cartproduct =CartProduct.objects.create(cart=cart_obj, product=product_obj, rate=product_obj.selling_price, quantity=1, sub_total=product_obj.selling_price) #4.2
                cart_obj.total_amount += product_obj.selling_price #4.3 make carts_total_amount equals to selling price of first products selected
                cart_obj.save()

        else: # this runs when you first enter and click add to cart button and create a cart object
            cart_obj = Cart.objects.create() #3.1 create new cart_object in database model class Cart tabel #if cart/cart_id doesnt exixt create a new cart object
            self.request.session["cart_id"] = cart_obj.id #3.2 after we create a cart_object we need to store the value of id of created cart_object into our session_storage as session_variable(cart_id) so that next time same cart_object can be used to products_items into it.
            # print("you have created a cart with cart_id ",cart_obj.id)
            # print("you have stored id of created cart into session_storage as session_variable(cart_id) ",cart_obj.id)
            cartproduct =CartProduct.objects.create(cart=cart_obj, product=product_obj, rate=product_obj.selling_price, quantity=1, sub_total=product_obj.selling_price) #3.3 now create an object of CartProduct class with all needed attributes and save it into database table
            cart_obj.total_amount += product_obj.selling_price #3.4 make carts_total_amount equals to selling price of first products selected
            cart_obj.save()

        return context






# class My_Cart(EcomMixin, TemplateView):
class My_Cart(TemplateView):
    template_name = "my_cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # method of parent class
        # print(context) # it already contain view key with vale
        # print(type(context))

        # get cart_id
        cart_id = self.request.session.get("cart_id", None) # session store and returns data in dictionanry form. So, key-pair

        #if_cart/cart_id exist get/fetch cart_obj or set cart_obj as None
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
        else:
            cart_obj=None
        # print(cart_obj.cartproduct_set.all())
        context['cart_obj'] = cart_obj # pass cart_object to template as item of context list
        # context = {'cart_obj':cart_obj} # you cal also wite it as this but it will not have extra_context if present in url_path
        # print(context)
        return context






class Manage_My_Cart(EcomMixin, View):
    def get(self, request, *args, **kwargs):
        cartproduct_id = self.kwargs['cartproduct_id'] #get cart_id
        action = request.GET.get('action') #get value of action parameter in url passed from my_cart.html
        cartproduct_obj = CartProduct.objects.get(id=cartproduct_id) #get a cartproduct_obj (cart with product coressponding to cart_id passed from my_cart.html)
        cart_obj = cartproduct_obj.cart

        # cart_obj1 = cartproduct_obj.cart #get the related cart
        # cart_id = request.session.get("cart_id", None) #get the related cart_id
        # if cart_id:
        #     cart_obj2 = Cart.objects.get(id=cart_id) # get cart object
        #     if cart_obj1 != cart_obj2:
        #         return redirect("my_cart")
        # else:
        #     return redirect("my_cart")

        if action == "plus":
            cartproduct_obj.quantity += 1
            cartproduct_obj.sub_total += cartproduct_obj.rate
            cartproduct_obj.save()
            cart_obj.total_amount += cartproduct_obj.rate
            cart_obj.save()
        elif action == "minus":
            cartproduct_obj.quantity -= 1
            cartproduct_obj.sub_total -= cartproduct_obj.rate
            cartproduct_obj.save()
            cart_obj.total_amount -= cartproduct_obj.rate
            cart_obj.save()
            if cartproduct_obj.quantity <= 0:
                cartproduct_obj.delete()
        elif action == "delete":
            cart_obj.total_amount -= cartproduct_obj.sub_total
            cart_obj.save()
            cartproduct_obj.delete()
        else:
            pass


        return redirect("my_cart")


class Clear_Cart(EcomMixin, View):
    def get(self, request, *args, **kwargs):
        cart_id = request.session.get("cart_id", None) # request current cart id store in session
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
            cart_obj.cartproduct_set.all().delete() # fetech all cart_products data using reverse relationship
            cart_obj.total_amount = 0
            cart_obj.save()

        # print(cart_obj.cartproduct_set)
        # print(cart_obj.cartproduct_set.all)
        # print(cart_obj.cartproduct_set.all())
        return redirect("my_cart")



class Checkout(EcomMixin, CreateView):
    template_name = "checkout.html"
    form_class = OrderForm
    success_url = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        # print(user)
        if request.user.is_authenticated and request.user.customer: #check where user is login or not and also if the logedin user is a customer or not
            print("user is logged in !")
        else:
            print("user in not logged in !")
            return redirect("/log_in/?next=/checkout/")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # get cart_id
        cart_id = self.request.session.get("cart_id", None) # session store and returns data in dictionanry form. So, key-pair

        #if_cart/cart_id exist get/fetch cart_obj or set cart_obj as None
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
        else:
            cart_obj=None
        context['cart_obj'] = cart_obj # pass cart_object to template as item of context list
        return context

    def form_valid(self, form):
        cart_id = self.request.session.get("cart_id")
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
            form.instance.cart = cart_obj
            form.instance.sub_total = cart_obj.total_amount
            form.instance.discount = 0
            form.instance.total = cart_obj.total_amount
            form.instance.order_status = "Order Received"
            del self.request.session['cart_id']
            # print(form.cleaned_data)
            payment_method = form.cleaned_data.get("payment_method")
            # print(payment_method)
            order_obj = form.save()
            # print(order_obj, order_obj.id, "*******************************")
            # print(form.instance, form.instance.id, "*******************************")
            if payment_method == "Khalti":
                return redirect(reverse("khalti_request") + "?order_id=" + str(order_obj.id))
            elif payment_method == "Esewa":
                return redirect(reverse("esewa_request") + "?order_id=" + str(order_obj.id))
            return redirect("customer_profile")
        else:
            return redirect("home")
        return super().form_valid(form)



def make_order(request):
    form = OrderForm()
    params = {'form':form}
    return render(request, "make_order.html", params)




#client_side integration
class KhaltiRequest(View): # view that will initiate the payment process #this class transfer the money
    def get(self, request, *args, **kwargs):
        order_id = request.GET.get("order_id")
        order_obj = Order.objects.get(id=order_id)
        context = {"order_obj":order_obj}
        return render(request, "khalti_request.html", context)



#server_side integration
class KhaltiVerify(View):  # view that will verify the payment process(avoid illigel activity)  #this class will verify/confirm if money is transfered or not !
    def get(self, request, *args, **kwargs):
        token = request.GET.get("token")
        amount = request.GET.get("amount")
        order_id = request.GET.get("order_id")
        # print(token, amount, order_id)

        url = "https://khalti.com/api/v2/payment/verify/"
        payload = {
            "token": token,
            "amount": amount
        }
        # print(token, amount)
        headers = {
            "Authorization": "Key test_secret_key_cf7256d62bfe461d8fcab8209e020766"
        }

        order_obj = Order.objects.get(id=order_id)

        response = requests.post(url, payload, headers = headers)
        # print(response)

        response_obj_dict = response.json()
        # print(response_obj_dict)

        if response_obj_dict.get("idx"):
            success = True
            order_obj.payment_done = True
            order_obj.save()
        else:
            success = False

        data = {
            "success_key": success
        }
        return JsonResponse(data)







#client_side
class EsewaRequest(View): # view that will initiate the payment process #this class transfer the money
    def get(self, request, *args, **kwargs):
        order_id = request.GET.get("order_id")
        order_obj = Order.objects.get(id=order_id)
        context = {"order_obj":order_obj}
        return render(request, "esewa_request.html", context)



#client_side
class EsewaVerify(View): # view that will initiate the payment process #this class transfer the money
    def get(self, request, *args, **kwargs):
        import xml.etree.ElementTree as ET #import xml
        order_id = request.GET.get("oid") #oid = pid = myorder_{{order_obj.id}}
        amount = request.GET.get("amt")
        ref_Id = request.GET.get("refId")
        # print("1", order_id, amount, ref_Id)

        url ="https://uat.esewa.com.np/epay/transrec"
        d = {
            'amt': amount,
            'scd': 'EPAYTEST', #merchat acconut in production level
            'rid': ref_Id,
            'pid': order_id,
        }
        resp = requests.post(url, d)
        # print("2", resp.text)

        root = ET.fromstring(resp.content)
        # print("3", root)
        # print("4", root[0])
        # print("5", root[0].text)

        status = root[0].text.strip()
        # print("6", status)
        print/("7", order_id)
        ord_id = order_id.split("_")[1]
        # print("8", ord_id)
        order_obj = Order.objects.get(id=ord_id)
        if status == "Success":
            # print("Success")
            order_obj.payment_done = True
            order_obj.save()
            return redirect("/")
        else:
            return redirect("/esewa_request/?order_id=" + ord_id)










#Veiw to create/register new Customer
class CustomerRegister(CreateView):
    template_name = "customer_register.html"
    form_class = CustomerRegistrationForm
    success_url = reverse_lazy("home")

    def form_valid(self, form1):
        username1 = form1.cleaned_data.get("custome_username")
        password1 =  form1.cleaned_data["custome_password"]
        email1 =  form1.cleaned_data.get("custome_email")
        django_user = User.objects.create_user(username1, email1, password1) # default_django_user #create new user/user_object in default django User_Model in database
        # django_user = User.objects.create_user(username1, password1, email1) # thie gave me error for two days
        # django_user = User.objects.create_user(username=username1, password=password1, email=email1) # I could have done this instead
        # print(django_user)
        # print(form1)f
        # print('Hi i am form.instance or instance of model of CustomerRegistrationForm', form1.instance)
        form1.instance.user = django_user # No no no till now Customer models object has not been created its just initialized. Here customer model object will  get created by buttom super().form_valid(form1) code.
        # new customer # create new customer/customer_object # assigning abouve created user to current form_instance of Customer_model which creates new customer/customer_object
        # here, form.instance means current instance of model of customer_model hold by form(CustomerRegistrationForm) and .user(form.instance.user) is attributes of Customer_model_class
        # and associating the cureent_django_user to user attribute of current_created_customer

        login(self.request, django_user)
        return super().form_valid(form1)

    def get_success_url(self):  #log_in success url router
        print(self.request.GET)
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            print(next_url)
            return next_url
        else:
            return self.success_url



class LogIn(FormView):
    template_name = "login.html"
    form_class = UserLogInForm
    success_url = reverse_lazy("home")

    # form_valid method is a post method which is available in CreateView and UpdateView
    def form_valid(self, form1):
        # print(form1) # form with filled fileds
        # print(form1.cleaned_data) # here cleaned_data is dictionary
        uname = form1.cleaned_data.get("login_username")
        pword =  form1.cleaned_data["login_password"] #QueryDict
        # print(uname, pword)
        django_user = authenticate(username=uname, password=pword)
        # print(django_user)
        # print(django_user.customer)
        # if django_user is not None and django_user.customer:
        if django_user is not None and Customer.objects.filter(user=django_user).exists():
            login(self.request, django_user)
        else:
            # return render(self.request, "login.html", {"form":UserLogInForm})
            return render(self.request, self.template_name, {"form":self.form_class, "error_var":"Invalid Credentials"})
        return super().form_valid(form1)

    def get_success_url(self): #log_in success url router
        print(self.request.GET)
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            print(next_url)
            return next_url
        else:
            return self.success_url




class LogOut(View):
    def get(self, request):
        logout(request)
        return redirect("home")






class CustomerProfile(TemplateView):
    template_name = "customer_profile.html"

    def dispatch(self, request, *args, **kwargs): #check login first before sending data
        user = request.user
        # print(user)
        if request.user.is_authenticated and request.user.customer: #check where user is login or not and also if the logedin user is a customer or not
            print("user is logged in !")
        else:
            print("user in not logged in !")
            return redirect("/log_in/?next=/customer_profile/")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs): #sending data
        context = super().get_context_data(**kwargs)
        customer = self.request.user.customer
        context["customer"] = customer
        orders = Order.objects.filter(cart__customer=customer)
        context["orders"] = orders
        return context






class CustomerOrderDetial( DetailView):
    template_name = "customer_order_detial.html"
    model = Order
    context_object_name = "order_obj"

    def dispatch(self, request, *args, **kwargs): #check login first before sending data
        user = request.user
        # print(user)
        # if request.user.is_authenticated and request.user.customer: #check where user is login or not and also if the logedin user is a customer or not
        if request.user.is_authenticated and Customer.objects.filter(user=user).exists(): #check where user is login or not and also if the logedin user is a customer or not
            # print("user is logged in !")
            order_id = self.kwargs["pk"]
            # print(order_id)

            order_obj = Order.objects.get(id=order_id)
            if request.user.customer != order_obj.cart.customer: #restrict user view other customers orders
                return redirect("/customer_profile/")
        else:
            # print("user in not logged in !")
            return redirect("/log_in/?next=/customer_profile/")
        return super().dispatch(request, *args, **kwargs)











class AdminLogIn(FormView):
    template_name = "admin/admin_login.html"
    form_class = UserLogInForm
    success_url = reverse_lazy('admin_dashboard')

    def form_valid(self, form1):
        uname = form1.cleaned_data.get("login_username")
        pword =  form1.cleaned_data["login_password"]
        django_user = authenticate(username=uname, password=pword)
        if django_user is not None and Admin.objects.filter(user=django_user).exists(): #check where user is login or not and also if the logedin user is a admin or not
            login(self.request, django_user)
        else:
            return render(self.request, self.template_name, {"form":self.form_class, "error_var":"Invalid Credentials"})
        return super().form_valid(form1)


class AdminRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs): #check login first before sending data
        if request.user.is_authenticated and Admin.objects.filter(user=request.user).exists(): #check where user is login or not and also if the logedin user is a admin or not
            pass
        else:
            return redirect("/admin_login/")
        return super().dispatch(request, *args, **kwargs)


class AdminDashboard(AdminRequiredMixin, TemplateView):
    template_name = "admin/admin_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pending_orders"] = Order.objects.filter(order_status="Order Received")
        return context



class AdminOrderDetial(AdminRequiredMixin, DetailView):
    template_name = "admin/admin_order_detial.html"
    model = Order
    context_object_name ="order_obj"

    def get_context_data(self, **kwargs): # get data from backend to frantend
        context = super().get_context_data(**kwargs)
        context["allstatus"] = ORDER_STATUS
        return context


class AdminAllOrders(AdminRequiredMixin, TemplateView):
    template_name = "admin/admin_dashboard.html"
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pending_orders"] = Order.objects.all()
        context["all_orders"] = True
        return context


# class AdminAllOrders(AdminRequiredMixin, ListView): # In case of ListView create new template
#     template_name = "admin/admin_dashboard.html"
#     queryset = Order.objects.all()
#     context_object_name ="order_obj"



class AdminOrderManage(AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        order_id = self.kwargs["pk"]
        order_obj = Order.objects.get(id=order_id)
        # print(request.POST)
        new_status = request.POST.get("status")
        # print(new_status)
        order_obj.order_status = new_status
        order_obj.save()
        return redirect(reverse_lazy("admin_order_detial", kwargs={"pk":order_id}))







class SearchProduct(TemplateView):
    template_name = "search_product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_keyword = self.request.GET["keyword"]
        results = Product.objects.filter(Q(title__icontains=url_keyword) | Q(desciption__icontains=url_keyword)  | Q(selling_price__icontains=url_keyword)  | Q(warranty__icontains=url_keyword)  | Q(return_policy__icontains=url_keyword))
        context["results"] = results
        return context






class AboutView(EcomMixin, TemplateView):
    template_name = "about.html"


class ContactView(EcomMixin, TemplateView):
    template_name = "contact.html"












