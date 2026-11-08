from django.urls import path
from apps.views import *

app_name = 'apps'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('logout/', UserLogOutView.as_view(), name='logout'),
]