from django import forms
from student.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "age", "email"]

    # Validation in Age
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18:
            raise forms.ValidationError("Age must be at least 18")
        return age