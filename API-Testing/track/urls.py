from django.urls import path
from track.views import Home

urlpatterns = [
    path('', Home.as_view(), name='home')
]
