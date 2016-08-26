from django.shortcuts import render
from cartt.cart import Cart
from parsxlx.models import Workbook

# Create your views here.

# def add_to_cart(request, product_id, quantity):
# 	product = Product.objects.get(id=product_id)
# 	cart = Cart(request)
# 	car.add(product, product.unit_price, quantity)

# def remove_from_cart(request, product_id):
# 	product = Product.objects.get(id=product_id)
# 	cart = Cart(request)
# 	cart.remove(product)

# def get_cart(request):
# 	return render_to_responce('cart.html', dict(cart=Cart(request)))

