from django.shortcuts import render


def index(request):
    # templates/food/index.html ni ko'rsatadi
    return render(request, 'food/index.html')


def order(request):
    # templates/food/order.html ni ko'rsatadi
    return render(request, 'food/order.html')
