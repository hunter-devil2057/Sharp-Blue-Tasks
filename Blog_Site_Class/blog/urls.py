from django.urls import path
from blog.views import *

urlpatterns = [
    # path('', HomeView.as_view(), name = 'Home'),     
    path('', BlogList.as_view(), name = 'BlogList'),  
    path('blog/<int:pk>/', BlogDetail.as_view(), name = 'BlogDetail'),  
    path('blog/<int:pk>/', BlogDetail.as_view(), name = 'BlogDetail'),  
    path('blog/<int:pk>/like/', PostLike.as_view(), name = 'PostLike'), 
    path('posts/search_results', Search.as_view(), name='Search'),
    path('posts/add', CreateBlog.as_view(), name='CreateBlog'), 
    path('posts/<int:pk>/edit', UpdateBlog.as_view(), name='UpdateBlog'), 
    path('posts/<int:pk>/delete', DeleteBlog.as_view(), name='DeleteBlog'),     
]
