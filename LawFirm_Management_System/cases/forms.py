from django import forms
from .models import Client, Lawyer, Case

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["first_name", "last_name", "email", "phone"]

class LawyerForm(forms.ModelForm):
    class Meta:
        model = Lawyer
        fields = ["first_name", "last_name", "email", "phone"]

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ["title", 'description', "status", "client", "lawyer"]