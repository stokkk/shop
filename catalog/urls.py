from django.urls import path

from . import views


urlpatterns = [
	path('', views.product_list, name="index"),
	path('sorte_by_name', views.product_list ),
	path('sorte_by_brand', views.product_list ),
	path('sorte_by_price', views.product_list ),
]