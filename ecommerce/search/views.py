from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

def search(request):
    products=None
    query=""
    if(request.method=="POST"):
        query=request.POST['q']
        print("query",query)
        if query:
         products=Product.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))
    return render(request,'search.html',{'query':query,'p':products})