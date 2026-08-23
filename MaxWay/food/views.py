import json

from django.shortcuts import redirect, render

from .models import Category, Product


def _cart_from_cookie(request):
	try:
		cart = json.loads(request.COOKIES.get('cart', '{}'))
	except (TypeError, json.JSONDecodeError):
		cart = {}

	return {str(product_id): int(quantity) for product_id, quantity in cart.items() if int(quantity) > 0}


def index(request):
	cart = _cart_from_cookie(request)
	products = Product.objects.select_related('category').all()
	cart_products = products.filter(id__in=cart.keys())
	total_price = sum(product.price * cart[str(product.id)] for product in cart_products)

	context = {
		'categories': Category.objects.all(),
		'products': products,
		'orders': [
			{'product': product, 'count': cart[str(product.id)]}
			for product in cart_products
		],
		'total_price': total_price,
	}
	return render(request, 'food/index.html', context)


def order_page(request):
	if request.method == 'POST':
		return redirect('index')

	cart = _cart_from_cookie(request)
	products = Product.objects.filter(id__in=cart.keys())
	context = {
		'orders': [
			{'product': product, 'count': cart[str(product.id)]}
			for product in products
		],
	}
	return render(request, 'food/order.html', context)
