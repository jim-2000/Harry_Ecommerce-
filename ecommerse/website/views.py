from django.shortcuts import render
from .import models


# Create your views here.

def home(request):
    store = models.product.objects.all()
    contex ={
        'store':store
    }
  
    return render(request ,"shop/index.html", contex)


def about(request):

    return render(request, "shop/about.html")
    
def contact(request):
    return HttpResponse("Hello  contact" )

    
def product(request):
    return HttpResponse("Hello  product ")

    
def search(request):
    return HttpResponse("Hello  search ")

    
def checkout(request):
    return HttpResponse("Hello  checkout")

    
def tracker(request):
    return HttpResponse("Hello  tracker")
