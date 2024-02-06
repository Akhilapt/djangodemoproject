from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from books.forms import bookform

from books.models import Book


def home(request):
     return  render(request,'home.html')

@login_required
def add(request):
    if(request.method=="POST"): #After submission
        t=request.POST['t']
        a = request.POST['a']
        p = request.POST['p']
        f=request.FILES['f']
        i=request.FILES['i']
        b=Book.objects.create(tittle=t,author=a,price=p,pdf=f,cover=i)
        b.save()
        return view(request)
    return render(request,'addbooks.html')

@login_required

def detail(request,p):
    b=Book.objects.get(id=p)
    return render(request,'bookdetail.html',{'b':b})

@login_required

def edit(request,p):
    b = Book.objects.get(id=p)
    if (request.method == "POST"):  # After Submission
        form = bookform(request.POST,request.FILES,isinstance=b)  # Create from object initialized with values inside request .POST
        if form.is_valid():
            form.save()  # Saves form object in db model book
            return view(request)


    form=bookform(isinstance=b)
    return render(request,'edit.html',{'form':form})

def search(request):
    b = None
    q = ""
    if (request.method == "POST"):
        q=request.POST['q']
        b=Book.objects.filter(Q(tittle__icontains=q)| Q(author__icontains=q))
    return render(request,'search.html',{'q':q,'b':b})

@login_required

def delete(request,p):
    b=Book.objects.get(id=p)
    b.delete()
    return view(request)


@login_required

def add1(request):
    if(request.method=="POST"):#After Submission
        form=bookform(request.POST)#Create from object initialized with values inside request .POST
        if form.is_valid():
            form.save()#Saves form object in db model book
            return view(request)

    form=bookform() #creates empty form object
    return render(request,'addbooks1.html',{'form':form})


@login_required

def fact(request):

     if(request.method=="POST"):
         num=int(request.POST['n'])
         f=1
         for i in range(1,num+1):
             f=f*i
         return render(request,'fact.html',{'fact':f})
         return render(request, 'fact.html')

@login_required

def view(request):
         k=Book.objects.all()
         return render(request,'view.html',{'b':k})

