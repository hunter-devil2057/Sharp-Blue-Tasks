from django.urls import path
from student.views import *

urlpatterns = [
    path('create/', StudentCreateView.as_view(), name='student_create'),
    path('', StudentListView.as_view(), name='student_list'),
    path('<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('<int:pk>/edit/', StudentUpdateView.as_view(), name='student_update'),
    path('<int:student_pk>/profile/', StudentProfileCreateUpdateView.as_view(), name='student_profile'),
]