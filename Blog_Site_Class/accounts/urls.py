from django.urls import path
from .views import Register, LogIn, LogOut, Dashboard

urlpatterns = [
    path('register/', Register.as_view(), name = 'register'),
    path('login/', LogIn.as_view(), name = 'login'), 
    path('logout/', LogOut.as_view(), name = 'logout'), 
    path('dashboard/', Dashboard.as_view(), name = 'dashboard'), 


]