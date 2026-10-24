from django.urls import path
from student.views import *

app_name = 'student'

urlpatterns = [
    path('add/', StudentCreate.as_view(), name='student_create'),
    path('', StudentList.as_view(), name='student_list'),
    path('details/<int:pk>/', StudentDetails.as_view(), name='student_details'),
    path('update/<int:pk>/', StudentUpdate.as_view(), name='student_update'),
    path('delete/<int:pk>/', StudentDelete.as_view(), name='student_delete'),
]
