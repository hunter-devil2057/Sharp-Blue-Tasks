from django.urls import path
from . import views
from .views import home, blog_list, blog_detail, post_like

urlpatterns = [
    path('', views.blog_list, name='list'),
    path('posts/<int:pk>/', views.blog_detail, name='detail'),
    path('like_posts/<int:pk>/', views.post_like, name='like'),
    path('posts/search_results', views.search, name='search'),
    path('posts/add', views.blog_create, name='blog_create'), 
    path('posts/<int:pk>/edit', views.blog_update, name='blog_update'), 
    path('posts/<int:pk>/delete', views.blog_delete, name='blog_delete'), 
]