from django.shortcuts import render, redirect #ดึงมาจากtemplats
from django.http import HttpResponse #เขียนบนกระดาน
from .models import Course, Student #importmodelclass
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
def homepage(request):
    #return HttpResponse('<h1>Hello San</h1>')
    return render(request, 'pages/home.html')

def Subjects(request):
    subj = Course.objects.all() #ดึงค่าจากdatabaseทั้งหมด
    context = {'subj':subj}

    return render(request, 'pages/subjects.html', context)

def Register(request):
    if request.method == 'POST':
        data = request.POST.copy()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')

        newuser = User()
        newuser.username = email
        newuser.first_name = first_name
        newuser.last_name = last_name
        newuser.email = email
        newuser.set_password(password)
        newuser.save()
        #from django.shortcuts import render, redirect
        return redirect(homepage)

    return render(request, 'pages/register.html')

def studentinfo(request,sID):

    print(sID)
    student_info = Student.objects.get(sID=sID)
    class_info = Course.objects.filter(attendStd = student_info)
    non_classinfo = Course.objects.exclude(attendStd = student_info).all()
    context = {'student_info': student_info, "class_info":class_info, "non_classinfo":non_classinfo,}

    return render(request, 'pages/class.html', context)
