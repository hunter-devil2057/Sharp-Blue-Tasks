from django.urls import path
from clients.views import *

app_name = "clients"

urlpatterns = [
    # **************** Client Page ****************
        path('client/', ClientListView.as_view(), name="client_list"), 
        path('client/create', ClientCreateView.as_view(), name="client_create"), 
        path('client/<int:pk>update', ClientUpdateView.as_view(), name="client_update"), 
        path('client/<int:pk>delete', ClientDeleteView.as_view(), name="client_delete"), 
]
