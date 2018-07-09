from django.shortcuts import render, redirect
# from my_test.models import Catalogs,Product
from .models import ProductShop
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProductForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import 

# def basе(request):
#     return redirect('/admin/')
# Create your views here.
# @login_required(login_url='/sale/sign-in')
# def sale(request):
#     alls =[item.catalog_name for item in Catalogs.objects.all()]
#     a={}
#     #top = Top.objects.all()[:SET_COUNT]
#     for name in alls:
#         a[name]={}
#         for prod in Product.objects.filter(product_catalog__catalog_name=name):
#             a[name][prod.pk]=prod.product_name
#     return render(request, "sale.html", {"alls": a})

# @login_required(login_url='/sale/sign-in')
def add_product(request,pid=""):
    product_form = ProductForm()
    if request.method=='POST':
        pro_form=ProductForm(request.POST)
        if pro_form.is_valid():
            ProductShop.objects.create(**pro_form.cleaned_data)
    return render(request, "add_product.html", {'pro_form':product_form, 'pid':pid})


def base(request, pid='Alex'):
    return render(request, "base.html",{'hello':pid})


def sign_up(request):
    user_form=UserCreationForm()
    if request.method=='POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            username=user_form.cleaned_data['username']
            password=user_form.cleaned_data['password1']
            new_user=User.objects.create_user(username=username,password=password)
            login(request, authenticate(username=username,password=password))
            return redirect('add_product/{}'.format("_".join(user_form.cleaned_data)))
    return render(request, "user_auth/sign-up.html", {'user_form':user_form})
