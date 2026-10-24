from django import forms
from lawyers.models import *

class LawyerForm(forms.ModelForm):
    class Meta:
        model = Lawyer
        fields = ["first_name", "last_name", "email", "phone"]