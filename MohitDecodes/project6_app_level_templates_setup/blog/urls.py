from django.urls import path
from blog import views

urlpatterns = [
    path('', views.post_list, name='blog_home'),
]
