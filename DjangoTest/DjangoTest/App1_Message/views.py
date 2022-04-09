from django.shortcuts import render, HttpResponseRedirect, HttpResponse, get_object_or_404
from django.contrib import messages

# Create your views here.

def message1(request):
    messages.success(request,'i am message1 !')
    return render(request, 'app_message/message.html')


def message2(request):
    messages.success(request,'i am message2 success !')
    messages.warning(request,'i am message2 warning !')
    messages.error(request,'i am message2 error !')
    messages.debug(request,'i am message2 debug !') #not print?
    messages.info(request,'i am message2 info !')
    return render(request, 'app_message/message.html')
