from django.urls import path
from shipments.views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
]
