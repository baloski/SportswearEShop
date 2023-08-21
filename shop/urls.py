from django.urls import path

from shop import views

app_name = "shop"

urlpatterns = [
	path('', views.home_page, name='home_page'),
	path('<slug:slug>', views.product_detail, name='product_detail'),
	path('search/', views.search, name='search'),
	path('filter/<slug:slug>/', views.filter_by_category, name='filter_by_category'),
]