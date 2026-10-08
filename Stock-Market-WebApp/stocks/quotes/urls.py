from django.urls import path
from . import views

# API Key: Z785HTJCYL211X9K

urlpatterns = [
    path('', views.home, name = "home"), 
    path('about/', views.about, name = "about"), 
]
