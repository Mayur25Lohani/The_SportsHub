from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password , check_password
from store.models.products import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View
from store.models.products import Product
from django import template

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html', {'products' : products} ) 

register = template.Library()







