from django.urls import path, include
from api.views import *

api_name = 'api_extract'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path("shipment/<str:shipment_number>/", ShipmentDetailView.as_view(), name="shipment_detail"),
]