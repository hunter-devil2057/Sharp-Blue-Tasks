from blog import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.home, name = 'home'), 
    path('post_details/<int:post_id>', views.post_details, name = 'post_details'), 
    path('user_profile/<str:username>', views.user_profile, name = 'user_profile'), 

    re_path(r'^article/(?P<year>[0-9]{4})/', views.article_by_year, name='article_by_year'),
]