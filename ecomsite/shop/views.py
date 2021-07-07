from django.shortcuts import render, redirect
from .models import Products
from django.forms import inlineformset_factory
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):
    product_objects = Products.objects.all()

    item_name = request.GET.get ('item_name')
    if item_name != '' and item_name is not None: 
        product_objects = product_objects.filter(title__icontains=item_name)
    return render(request,'shop/index.html',{'product_objects':product_objects})

def about(request):
    product_objects = Products.objects.all()
    return render(request, 'shop/about.html',{'products_objects':product_objects})

def categorias(request):
    product_objects = Products.objects.all()
    return render(request, 'shop/categorias.html',{'products_objects':product_objects})

def contacto(request):
    product_objects = Products.objects.all()
    return render(request, 'shop/contacto.html',{'products_objects':product_objects})

def detail(request, id):
    product_objects = Products.objects.get(id=id)
    return render(request, 'shop/detail.html',{'products_objects':product_objects})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, username)
            redirect(index)
    context = {}
    return render(request, 'shop/login.html', context)

def register(request):

    form = CreateUserForm()
    if request.method == 'POST': 
       form = CreateUserForm(request.POST)
       if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'shop/register.html', context) 



        