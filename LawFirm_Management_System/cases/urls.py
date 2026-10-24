from django.urls import path
from cases.views import *
# from . import views

app_name = "cases"

urlpatterns = [
    # **************** Cases Page ****************
    path('case/', CaseListView.as_view(), name="case_list"), 
    path('case/create', CaseCreateView.as_view(), name="case_create"), 
    path('case/<int:pk>update', CaseUpdateView.as_view(), name="case_update"), 
    path('case/<int:pk>delete', CaseDeleteView.as_view(), name="case_delete"), 
]
