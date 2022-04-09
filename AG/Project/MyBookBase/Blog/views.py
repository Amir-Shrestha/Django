from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import Post
from .forms import PostForm, DocumentForm, SubscribeForm, CommentForm, RegisterForm
from django.core.paginator import Paginator, PageNotAnInteger

# Create your views here.
def home(request):
    return HttpResponse('I am Home HttpResponse !')

def blogindex(request):
    return render(request, 'blogindex.html',{})

def post_list(request):
    # print('view called')
    # posts = Post.objects.all().order_by('id') # hold all posts
    if request.user.is_authenticated:
        posts = Post.objects.filter(author=request.user) # hold all author_posts
    else:
        posts = Post.objects.all().order_by('id') # hold all posts
    paginator = Paginator(posts, 2, orphans=1) # hold/split all_pages, 3 posts per page
    page_number = request.GET.get('page') # hold page number  #get value of page_key from urls_parameter that holds key-value paired as dictionary.
    page_obj = paginator.get_page(page_number)
    try:
        page_obj = paginator.page(page_number) # holds a single page with provided page number
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    return render(request, 'post_list.html', {'page_number':page_number, 'page_posts':page_obj})


def about(request):
    return render(request, 'about.html', {})

def a_post(request,post_id):
    apost = get_object_or_404(Post, id=post_id) #Not_QuerySet , its object of Post model_class
    comments = apost.comments.filter(active=True)
    new_comment = None

    #If add comment, in comment form, posted comment for current post.
    if request.method=='POST':
        comment_form = CommentForm(request.POST)
        if comment_form .is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = apost
            new_comment.save()
            #render to a_post page with empty comment form

    comment_form = CommentForm() #render to a_post page with empty comment form
    params = {'apost':apost, 'comments':comments, 'comment_form':comment_form, 'new_comment':new_comment}
    return render(request, 'a_post.html', params)

def create_post(request):
    if request.method=='POST':
        form_value_obj = PostForm(request.POST, request.FILES) #filled_form_with_data #object_of_PostForm_class in forms.py module
        if form_value_obj .is_valid():
            post = form_value_obj.save(commit=False) # when we save the filled form then it creates instance of Post_model_class  #object_of_Post_class in models.py module.
                                                     # as form_value_obj is object of PostForm_class and PostForm_class holds the form of Post_model_class.
                                                     #  Therefore post is instance/object of  Post_model_class.
            post.author = request.user #set author attribute as current_login_user to object/instance of Post_model #associating newly_created_post with user_currently_login
            post.published_date = timezone.now()
            post.save()
            return redirect('apost', post_id=post.id) #post.id is unique primary key of post that is created automatically
    else:
        form_value_obj  = PostForm()
    print(form_value_obj)
    return render(request, 'create_post.html', {'form_obj':form_value_obj})




def upload(request):
    if request.method == 'POST':
        doc_obj = DocumentForm(request.POST, request.FILES)
        if doc_obj.is_valid():
            doc_obj.save()
            return redirect('post_list')
    else:
        doc_obj = DocumentForm()
    return render(request, 'add_file.html', {'doc_obj':doc_obj})




from MyBook.settings import EMAIL_HOST_USER
from django.core.mail import send_mail




def subscribe(request):
    if request.method == 'POST':
        sub = SubscribeForm(request.POST)
        # print(sub)
        # print(type(sub))
        # print("First ", sub['Email'])
        subject = "Welcome to Achiever's Group"
        message = 'Demo email message !'
        recepient = sub['Email'].value()
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
        return render(request, 'success.html', {'recepient':recepient})

    sub = SubscribeForm()
    return render(request, 'email.html', {'form':sub})





def register_method(response):
    if response.method == "POST":
        new_rgister = RegisterForm(response.POST)
        if new_rgister.is_valid():
            new_rgister.save()
            # msg = ''
            # return redirect('register_path',{'msg':msg})
            return redirect('register_path')
    form = RegisterForm()
    return render(response, 'register/signup.html', {'form':form})
