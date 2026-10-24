from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from lawyers.models import *
from lawyers.forms import *

# Create your views here.
# Lawyer View
class LawyerListView(ListView):
    model = Lawyer
    template_name = 'lawyers/lawyer_list.html'

class LawyerCreateView(CreateView):
    model = Lawyer
    form_class = LawyerForm
    template_name = 'lawyers/lawyer_form.html'
    success_url = '/lawyers/'

class LawyerUpdateView(UpdateView):
    model = Lawyer
    form_class = LawyerForm
    template_name = 'lawyers/lawyer_form.html'
    success_url = '/lawyers/'

class LawyerDeleteView(DeleteView):
    model = Lawyer
    template_name = 'lawyers/lawyer_confirm_delete.html'
    success_url = reverse_lazy("cases:lawyer_list")