from django.shortcuts import render
from datetime import datetime
import json


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

def products(request, id=None):
    context = {
        'title': 'products',
        'now': datetime.now().year,
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'mainapp/products.html', context)





