from django import forms
from student.models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "email", "enrollment_date", "department", "courses"]
        widgets = {
            "enrollment_date": forms.DateInput(attrs={'type': 'date'}), 
            'courses': forms.CheckboxSelectMultiple()       # yeuta stds le many course study garni vayeko vayera
        }

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ["phone", "address", "dob", "bio"]
        widgets = {
            "dob": forms.DateInput(attrs={'type': 'date'}), 
        }
