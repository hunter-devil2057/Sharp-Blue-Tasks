from django.urls import path
from core.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='Home'), 
    path('detail/', DetailView.as_view(), name='Details')
]
