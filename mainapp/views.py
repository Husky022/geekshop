from django.shortcuts import render
from datetime import datetime
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.cache import cache_page


from mainapp.models import Product, ProductCategory

def get_products_data():
    with open('./mainapp/fixtures/products.json', encoding='utf-8') as file:
        products_data = json.load(file)
        products = products_data['products']
        return products


# Create your views here.


def base(request):
    context = {
        'now': datetime.now().year
    }
    return render(request, 'mainapp/base.html', context)


def index(request):
    context = {
        'title': 'geekshop',
        'now': datetime.now().year
    }
    return render(request, 'mainapp/index.html', context)



def products(request, category_id=None, page=1):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    per_page = 3
    paginator = Paginator(products.order_by('price'), per_page)
    products_paginator = paginator.page(page)
    context = {'categories': ProductCategory.get_all(), 'products': products_paginator}
    return render(request, 'mainapp/products.html', context)





