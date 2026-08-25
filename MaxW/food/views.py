from django.shortcuts import render
from .models import Category, Product


def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'food/index.html', {"products": products, "categories": categories})


def order(request):
    return render(request, 'food/order.html')