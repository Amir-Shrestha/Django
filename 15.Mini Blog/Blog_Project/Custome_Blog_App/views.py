


from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .forms import SignUpForm, LogInForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post
from django.contrib.auth.models import Group

# Create your views here.

warning_msg = 'You have to Login First !!!'

def home(request):
    posts = Post.objects.all()
    return render(request, 'custome_blog_app/home.html', {'posts':posts})

def about(request):
    return render(request, 'custome_blog_app/about.html' )

def contact(request):
    return render(request, 'custome_blog_app/contact.html' )

def dashboard(request):
    if request.user.is_authenticated:
        # posts = Post.objects.filter(author=request.user)
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        groups = user.groups.all()
        return render(request, 'custome_blog_app/dashboard.html', {'posts':posts, 'full_name':full_name, 'groups':groups})
    else:
        messages.warning(request, warning_msg)
        return HttpResponseRedirect('/login/')

def signup_user(request):
    if request.method == "POST":
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user  = signup_form.save()
            group = Group.objects.get(name="Author")
            user.groups.add(group)
            success_msg = 'Congratulations !!!'+ signup_form.cleaned_data['username'] + ', You are an Author now.'
            messages.success(request, 'susccess msg')
            print(messages.get_level(request))
            messages.info(request, success_msg)
            print(messages.get_level(request))
            # messages.add_message(request, messages.SUCCESS, success_msg)
    else:
        signup_form = SignUpForm()
    return render(request, 'custome_blog_app/signup.html', {'signup_form':signup_form})

def login_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            login_form = LogInForm(request=request, data=request.POST)
            if login_form.is_valid():
                uname = login_form.cleaned_data['username']
                upass = login_form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                success_msg = uname + ', Logged In Successfully !'
                messages.success(request, success_msg)
                return HttpResponseRedirect('/dashboard/')
        else:
            login_form = LogInForm()
        return render(request, 'custome_blog_app/login.html', {'login_form':login_form})
    else:
        return HttpResponseRedirect('/dashboard/')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")

def create_apost(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            post_form = PostForm(request.POST)
            if post_form .is_valid():
                title = post_form.cleaned_data['title']
                description = post_form.cleaned_data['description']
                new_post = Post(title=title, description=description)
                new_post.save()
        post_form  = PostForm()
        return render(request, 'custome_blog_app/create_post.html', {'post_form':post_form})
    else:
        messages.warning(request, warning_msg)
        return HttpResponseRedirect('/login/')



def update_apost(request, id):
    if request.user.is_authenticated:
        if request.method=='POST':
            old_post = Post.objects.get(pk=id)
            updated_post_form = PostForm(request.POST, instance=old_post) #request.POST takes over old_post
            if updated_post_form.is_valid():
                updated_post_form.save()
                return HttpResponseRedirect('/dashboard')
        old_post = Post.objects.get(pk=id)
        old_post_form = PostForm(instance=old_post) #old_post_form with data
        return render(request, 'custome_blog_app/update_post.html', {'old_post_form':old_post_form})

    else:
        messages.warning(request, warning_msg)
        return HttpResponseRedirect('/login/')

def delete_apost(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            del_apost = Post.objects.get(pk=id)
            del_apost.delete()
            return HttpResponseRedirect('/dashboard')
    else:
        messages.warning(request, warning_msg)
        return HttpResponseRedirect('/login/')

