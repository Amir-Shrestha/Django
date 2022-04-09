from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from .models import Product, Contact, Orders, OrderUpdate
from math import ceil
import json
from django.urls import reverse

# Create your views here.



def index(request):
    Category_Slides_List = [] #list # list that contain another list of products of distinct category
    catagories_of_all_product = Product.objects.values('category', 'id') #QuerySet    # QuerySet that contains dictionary key-value paired of category and id of all products category
    distinct_categories = {item['category'] for item in catagories_of_all_product} #Set   # Set of distinct category   # Set comprehensive
    for category in distinct_categories: # here category is str
        distinct_category_products  = Product.objects.filter(category=category) #QuerySet  #Retrieving specific objects with filters/category #fetch product with category    # QuerySet that contains all products of same category
        n = len(distinct_category_products) #int    #total number of products of distinct category
        number_of_slide_in_crousel = n // 4 + ceil(n / 4 - n // 4) #int #total number of slides with 4 products in each of distinct category
        Category_Slides_List.append([distinct_category_products, range(1,number_of_slide_in_crousel), number_of_slide_in_crousel])    #list     # append list to list    # list that contain another list of products of distinct category
    params = { 'Category_Slides_List' : Category_Slides_List } #dictionary     # dictionary of parameters to be pass in te,plates
    return render(request, 'shop/index.html',params)




def about_us(request):
    return render(request, 'shop/about.html')




def contact_us(request):
    if request.method=="POST":
        # print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        description = request.POST.get('desc', '')
        # print(name, email, phone, description)
        contact = Contact(contact_name=name, contact_email=email, contact_phone=phone, contact_address=address, contact_desciption=description )
        contact.save()
        send=True
        return render(request, 'shop/contact.html', {'send':send, 'name':name})
    return render(request, 'shop/contact.html')




def product_view(request, pro_id):
    # product = Product.objects.filter(product_id=pro_id) #as we have not set product_id as Primary Key in our model here django automatially set it Primary Key as id field so id instead of product_id
    product = Product.objects.filter(id=pro_id) #QuerySet_list with only one product
    return render(request, 'shop/product_view.html', {'product_item':product[0]})




def checkout(request):
    return render(request, 'shop/check_out.html')

def make_order(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        amount= request.POST.get('total', '')
        print(items_json)
        print(amount)
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')
        print(request.POST.get('phone', ''))
        print(request.POST.get('name', ''))

        order = Orders(items_json= items_json, amount=amount, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save() #save order
        update_order = OrderUpdate(order_id=order.order_id, update_desc="Order has been placed !")
        update_order.save() #save order update tracker
        thank=True
        id=order.order_id
        return render(request, 'shop/make_order.html', {'thank':thank, 'id':id})
        # return redirect(reverse("khaltirequest"))
    total = request.GET['totalPrice2']
    items_json = request.GET['itemsJson']
    params = {'total':total, 'items_json':items_json}
    return render(request, 'shop/make_order.html', params)




def search(request):
    query= request.GET.get('search')
    # print(query)
    Category_Slides_List = [] #list # list that contain another list of products of distinct category
    catagories_of_all_product = Product.objects.values('category', 'id') #QuerySet    # QuerySet that contains dictionary key-value paired of category and id of all products category
    # print(catagories_of_all_product)
    distinct_categories = {item['category'] for item in catagories_of_all_product} #Set   # Set of distinct category   # Set comprehensive
    # print(distinct_categories)
    for category in distinct_categories: # here category is str
        distinct_category_products_temp  = Product.objects.filter(category=category) #QuerySet  #Retrieving specific objects with filters/category #fetch product with category    # QuerySet that contains all products of same category
        # print(distinct_category_products_temp)
        distinct_category_products = [item for item in distinct_category_products_temp if searchMatch(query, item)] #distinct_category_products according to search #list_comprehensive
        # print(distinct_category_products)
        n = len(distinct_category_products) #int    #total number of products of distinct category according to search
        number_of_slide_in_crousel = n // 4 + ceil(n / 4 - n // 4) #int #total number of slides with 4 products in each of distinct category
        if len(distinct_category_products)!= 0:
            Category_Slides_List.append([distinct_category_products, range(1,number_of_slide_in_crousel), number_of_slide_in_crousel])    #list     # append list to list    # list that contain another list of products of distinct category
    params = { 'Category_Slides_List' : Category_Slides_List, "msg":"" } #dictionary     # dictionary of parameters to be pass in te,plates
    if len(Category_Slides_List)==0 or len(query)<4:
        params={'msg':"No result found! Please make sure to enter relevant search query!"}
    return render(request, 'shop/index.html',params)




def searchMatch(query, item):
    if query.lower() in item.product_name.lower() or query.lower() in item.category.lower():
        return True
    else:
        return False




def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                order_update_objs = OrderUpdate.objects.filter(order_id=orderId) #QuerySet of objects of order_updated
                order_updates_list = [] #list of dictionary of order_updated key-value-pair(text,time)
                for order_updates_obj in order_update_objs:
                    order_updates_list.append({'text': order_updates_obj.update_desc, 'time': order_updates_obj.timestamp}) #append dictionary of order_updated key-value-pair(text,time) to list(order_updates_list)
                    # response = json.dumps([order_updates_list, order[0].items_json], default=str) # convert list(order_updates_list) into string(response),  like Javascript array
                    response = json.dumps({"status":"success", "updates":order_updates_list, "itemsJson":order[0].items_json}, default=str) # convert dictionary into string/JSON(response),  like Javascript array
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"No Items !"}')
        except Exception as e:
            return HttpResponse('{"status":"Error !"}')
    return render(request, 'shop/tracker.html')




def esewa(request):
    pass










from django.views.generic import View

class Khalti(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "khalti.html", context)
