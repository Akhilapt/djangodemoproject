from django.contrib.auth import login,authenticate,logout

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from students.models import CustomUser
# Create your views here.

from students.models import Students
from django.contrib.auth.models import User
from django.http import HttpResponse
def add(request):
    return render(request,'addstudents.html')
def register(request):
    if(request.method=="POST"):
        un=request.POST['un']
        pa= request.POST['pa']
        cp=request.POST['cp']
        fn= request.POST['fn']
        ln= request.POST['ln']
        em= request.POST['em']
        pl=request.POST['pl']
        ph=request.POST['ph']

        if(pa==cp):
           user=CustomUser.objects.create_user(username=un,password=pa,first_name=fn,last_name=ln,email=em,place=pl,phone=ph)
           user.save()
           return redirect('books:home')
        else:
            return HttpResponse("Passwords are not same")

    return  render(request,'register.html')

def user_login(request):
    if(request.method=="POST"):
        un=request.POST['un']
        pa=request.POST['pa']
        user=authenticate(username=un,password=pa)
        if user:
            login(request,user)
            return redirect('books:home')
        else:
            return HttpResponse("Invalid credentials")
    return render(request,'login.html')

@login_required()
def user_logout(request):
    logout(request)
    return redirect('students:login')

def view(request):
    k = Students.objects.all()
    return render(request, 'viewstudents.html', {'b': k})
