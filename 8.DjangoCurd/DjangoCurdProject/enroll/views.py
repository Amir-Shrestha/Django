from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import StudentForm
from .models import Student

# Create your views here.

def addshow(request):
    print(request)
    if request.method =='POST':
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            name1 = student_form.cleaned_data['name']
            email1 = student_form.cleaned_data['email']
            password1 = student_form.cleaned_data['password']
            register = Student(name=name1, email=email1, password=password1)
            register.save()
            return HttpResponseRedirect('/') # solve problem that save data every time reload browser

    student_form = StudentForm()
    all_students = Student.objects.all() #querySet
    no_std = len(all_students)
    return render(request, 'enroll/addandshow.html', {'student_form':student_form, 'all_students':all_students, 'no_std':no_std})

def editstd(request, id):
    std = Student.objects.get(id=id) #intacne of Student ModelClass
    if request.method == "POST":
        # print(std)
        # Creating a form to change an existing post.
        student_form = StudentForm(request.POST, instance=std) #edit row #data submitted by update form takes over data of model row
        # print(student_form)
        if student_form.is_valid():
            student_form.save()
            return HttpResponseRedirect('/')

    # Creating a form to add an post.
    student_detial_form = StudentForm(instance=std) #form with data
    return render(request, 'enroll/updatestudent.html', {'student_detial_form':student_detial_form})


def delete_std(request, id):
    if request.method == "POST":
        std = Student.objects.get(id=id)
        std.delete()
        return HttpResponseRedirect('/')