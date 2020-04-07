from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Product
# Create your views here.

def by_name(product):
	return product.name 

def by_brand(product):
	return product.brand 

def by_price(product):
	return product.price

def product_list(request,sort_slot="sorte_by_name"):
	
	if sort_slot == "sorte_by_name":
		products = Product.objects.order_by("name")
	elif sort_slot == "sorte_by_brand":
		products = Product.objects.order_by("brand")
	elif sort_slot == "sorte_by_price":
		products = Product.objects.order_by("price")
	
	return render(request, 'catalog/index.html', {'products': products })

	