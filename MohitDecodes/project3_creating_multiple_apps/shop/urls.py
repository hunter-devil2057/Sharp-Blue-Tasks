from shop import views
from django.urls import path

urlpatterns = [
    path('', views.shop_home, name='shop_home'), 
    path('products/', views.shop_product, name = 'shop_product'),
]