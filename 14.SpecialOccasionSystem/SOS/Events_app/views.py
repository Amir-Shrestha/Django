from django.shortcuts import render, HttpResponseRedirect, HttpResponse, get_object_or_404, redirect
from .forms import SignUpForm, LogInForm, EventForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Event, Contact, Profile
from django.contrib.auth.models import Group
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger
from django.contrib.auth.models import User

# Create your views here.

warning_msg = 'You have to Login First !!!'

def home(request):
    # events = Event.objects.all()
    events = Event.objects.order_by('-published_date')
    paginator = Paginator(events, 4)
    # paginator = Paginator(events, 3, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    try:
        page_obj = paginator.page(page_number) # holds a single page with provided page number
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    messages.success(request, 'Welcome to our SpecialOccassion System !!!')
    return render(request, 'events_app/home.html', {'page_number':page_number, 'page_events':page_obj})

def about(request):
    return render(request, 'events_app/about.html' )

def dashboard(request):
    if request.user.is_authenticated:
        print('2')
        if str(request.user) == "admin":
            print('3')
            events = Event.objects.all()
        else:
            print('4')
            events = Event.objects.filter(author=request.user)
        user = request.user
        full_name = user.get_full_name()
        groups = user.groups.all()
        profile = get_object_or_404(Profile, user=request.user)
        usertype = str(request.user)
        authors = User.objects.all()
        return render(request, 'events_app/dashboard/dashboard.html', {'events':events, 'full_name':full_name, 'groups':groups, 'profile':profile, 'usertype':usertype, 'authors':authors })
    else:
        messages.warning(request, 'Excuse me, You have to Login First !!!')
        return HttpResponseRedirect('/login/')


def profile_update(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            profile_form = ProfileForm(request.POST, instance=request.user)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Profile Updated !')
        profile_form = ProfileForm(instance=request.user)
        profile = get_object_or_404(Profile, user=request.user)
        usertype = str(request.user)
        return render(request, 'events_app/dashboard/profile_update.html', {'name':request.user, 'profile':profile, 'profile_form':profile_form, 'usertype':usertype})
    else:
        return HttpResponseRedirect('/login')

def profile(request, id):
    author = get_object_or_404(User, id=id)
    if author:
        host = get_object_or_404(Profile, user=author)
        if request.user.is_authenticated:
            usertype = str(request.user)
            profile = get_object_or_404(Profile, user=request.user)

            login_user = str(request.user)
            event_author = str(author)
            if login_user == event_author:
                edit_profile =True
            else:
                edit_profile =False

            return render(request, 'events_app/dashboard/profile.html', {'name':request.user, 'profile':profile, 'usertype':usertype, 'author':author, 'host':host, 'edit_profile':edit_profile})
        else:
            # return HttpResponse('hi')
            return render(request, 'events_app/dashboard/profile.html', {'author':author, 'host':host})
    else:
        messages.warning(request, 'No any author with id = '+str(event_id))
        return redirect('/')




def event(request,event_id):
    event = get_object_or_404(Event, event_id=event_id) #Not_QuerySet , its object of Post model_class
    if event:
        print(event)
        return render(request, 'events_app/event.html', {'event':event})
    else:
        messages.warning(request, 'No any post with id = '+str(event_id))
        return redirect('/')





def signup_user(request):
    # print(request)
    # print(request.method)
    # print(request.GET)
    # print(request.POST)
    if request.method == "POST":
        # print('2')
        signup_form = SignUpForm(request.POST) # instance/object of FormClass(SignUpForm) with fields filled with data
        # print(type(signup_form))
        # print(signup_form)
        # print(signup_form.__dict__.keys())
        # print(signup_form.cleaned_data['username'], "*************************")
        # print(request.POST['username'], "*************************")
        if signup_form.is_valid():
            print('3')

            #create_account
            user  = signup_form.save() #save the filled_form_object as object of model class and return model_object # Here user is object of User ModelClass(class Meta:model=User in SignUpForm)

            #assign user to a group
            group_role = Group.objects.get(name="Author") #select group
            user.groups.add(group_role) # assign newly registered user to a selected group
            success_msg = 'Congratulations !!!'+ signup_form.cleaned_data['username'] + ', You are an Author now.'
            messages.success(request, success_msg)

            #login
            uname = signup_form.cleaned_data['username']
            upass = signup_form.cleaned_data['password1']
            print(uname, upass)
            user = authenticate(username=uname, password=upass)
            if user is not None:
                print('4')
                login(request, user)
                print('5')
                success_msg = uname + ', Logged In Successfully !'
                messages.success(request, success_msg)
                return redirect('login')
        else:
             messages.warning(request, 'not valid data')
    print('1')
    signup_form = SignUpForm() # instance/object of FormClass(SignUpForm) with empty fields
    # print(signup_form)
    # print(type(signup_form))
    messages.info(request, 'Please create your account !!!')
    return render(request, 'events_app/signup.html', {'signup_form':signup_form})


def login_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            login_form = LogInForm(request=request, data=request.POST)
            # print(login_form)
            # print(login_form.__dict__.keys())
            if login_form.is_valid():
                uname = login_form.cleaned_data['username']
                upass = login_form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                success_msg = 'Logged In as ' + uname + ' Successfully !'
                messages.success(request, success_msg)
                return HttpResponseRedirect('/dashboard/')
        else:
            login_form = LogInForm()
        return render(request, 'events_app/login.html', {'login_form':login_form})
    else:
        return HttpResponseRedirect('/dashboard/')

def logout_user(request):
    logout(request)
    messages.warning(request, 'Logged Out Successfully !')
    return HttpResponseRedirect("/")




def create_event(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            events_form = EventForm(request.POST, request.FILES)
            if events_form .is_valid():
                event_title = events_form.cleaned_data['title']
                event_description = events_form.cleaned_data['description']
                event_date = events_form.cleaned_data['event_date']
                event_thumbnail = events_form.cleaned_data['thumbnail']
                event_category = events_form.cleaned_data['category']
                new_event = Event(title=event_title, description=event_description, event_date=event_date, thumbnail=event_thumbnail, category=event_category)
                # print(new_event)
                new_event.author = request.user
                new_event.published_date = timezone.now()
                # print(new_event)
                new_event.save()
                # print(new_event)
                messages.success(request, 'Post created Successfully !!!')
                # return render(request, 'events_app/event.html new_event.event_id')
            else:
                messages.warning(request, 'Invalid Created Post fields !!!')
        new_event  = EventForm()
        profile = get_object_or_404(Profile, user=request.user)
        usertype = str(request.user)
        authors = User.objects.all()
        # print(authors)
        # messages.info(request, 'Please Create a post !!!')
        return render(request, 'events_app/dashboard/create_event.html', {'new_event':new_event, 'profile':profile, 'usertype':usertype, 'authors':authors })
    else:
        messages.warning(request, 'Please LogIn first !!!')
        return HttpResponseRedirect('/login/')


def authorlist(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        usertype = str(request.user)
        authors = User.objects.all()
        return render(request, 'events_app/dashboard/authorlist.html', {'profile':profile, 'usertype':usertype, 'authors':authors })
    else:
        messages.warning(request, 'Please LogIn first !!!')
        return HttpResponseRedirect('/login/')




def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        address = request.POST['address']
        message = request.POST['message']
        # print(name, email, number, message,address)
        # print(timeStamp) #error->name 'timeStamp' is not defined
        if len(name)<2 or len(email)<3 or len(number)<10 or len(message)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            feedback = Contact(name=name, email=email, number=number, address=address, message=message)
            # print(feedback)
            feedback.save()
            messages.success(request, "Your message has been successfully sent !!!")
            return HttpResponseRedirect('/')
    return render(request, 'events_app/contact.html' )








def update_event(request, event_id):
    if request.user.is_authenticated:
        if request.method=='POST':
            old_event = Event.objects.get(pk=event_id)
            updated_events_form = EventForm(request.POST, instance=old_event) #request.Events takes over old_Events
            if updated_events_form.is_valid():
                updated_events_form.save()
                messages.success(request, "Editted Succefully !!!")
                return HttpResponseRedirect('/dashboard')
        old_event = Event.objects.get(pk=event_id) #object of old post
        old_events_form = EventForm(instance=old_event) #form of object of old post with data  #old_events_form with data
        profile = get_object_or_404(Profile, user=request.user)
        return render(request, 'events_app/dashboard/update_event.html', {'old_events_form':old_events_form, 'profile':profile})
    else:
        messages.warning(request, 'You have to Login First !!!')
        return HttpResponseRedirect('/login/')







def delete_event(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            del_aEvents = Event.objects.get(pk=id)
            del_aEvents.delete()
            messages.error(request, 'Post deleted !')
            return HttpResponseRedirect('/dashboard')
    else:
        messages.warning(request, 'You have to Login First !!!')
        return HttpResponseRedirect('/login/')


