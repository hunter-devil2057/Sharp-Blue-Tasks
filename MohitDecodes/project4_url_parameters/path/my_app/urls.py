from my_app import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'home'), 
    path('post_details/<int:post_id>', views.post_details, name = 'post_details'), 
    path('user_profile/<str:username>', views.user_profile, name = 'user_profile'), 
]