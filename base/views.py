from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item

# Create your views here.

def index(request):
    context = {
        'items': Item.objects.all()
    }
    return render (request,"base/index.html",context)

def sales(request):
    context = {
        'items': Item.objects.all()
    }
    return render (request,"base/sales.html",context)

def about(request):
    return render (request,"base/about.html")

def contact(request):
    return render (request,"base/contact.html")

def login(request):
    return render (request,"base/login.html")

def signup(request):
    return render (request,"base/signup.html")

def product(request):
    context = {
        'items': Item.objects.all()
    }
    return render (request,"base/product.html",context)


class HomeView(ListView):
    model = Item
    template_name = "base/index.html"

class ItemDetailView(DetailView):
    model = Item
    template_name = "base/product.html"