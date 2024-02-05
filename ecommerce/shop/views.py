from django.shortcuts import render,redirect
from shop.models import Category,Product
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
def allcategories(request):
    c=Category.objects.all()
    return render(request,'category.html',{'c':c})
def allproducts(request,p):
    c=Category.objects.get(name=p)
    p=Product.objects.filter(category=c)
    return render(request,'products.html',{'c':c,'p':p})

def details(request,c):
    p=Product.objects.get(name=c)
    return render(request,'detail.html',{'p':p})

def register(request):
    if(request.method=="POST"):
        un=request.POST['un']
        pa= request.POST['pa']
        cp=request.POST['cp']
        fn= request.POST['fn']
        ln= request.POST['ln']
        em= request.POST['em']


        if(pa==cp):
           user=User.objects.create_user(username=un,password=pa,first_name=fn,last_name=ln,email=em)
           user.save()
           return redirect('shop:allcat')
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
            return redirect('shop:allcat')
        else:
            return HttpResponse("Invalid credentials")
    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return user_login(request)
