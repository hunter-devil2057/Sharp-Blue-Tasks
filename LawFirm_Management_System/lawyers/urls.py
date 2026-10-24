from django.urls import path

from lawyers.views import *

app_name = "lawyers"

urlpatterns = [
    path('details/', LawyerListView.as_view(), name="lawyer_list"), 
    path('lawyer/create', LawyerCreateView.as_view(), name="lawyer_create"), 
    path('lawyer/<int:pk>update', LawyerUpdateView.as_view(), name="lawyer_update"), 
    path('lawyer/<int:pk>delete', LawyerDeleteView.as_view(), name="lawyer_delete"), 
]
