from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required = True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Email Validation
        def clean_email(self):
            email = self.cleaned_data.get('email')
            # Check gareko, whether email le pahiley register gareko xata?? vanera
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Email already exists")
            return email
        widgets = {
            'username': forms.TextInput(
                attrs = {
                    'class': 'form-control', 
                    'placeholder': 'Enter Username', 
                    'required': True, 
                }
            ), 
            'email': forms.EmailInput(
                attrs = {
                    'class': 'form-control', 
                    'placeholder': 'Enter Email Address', 
                    'required': True,
                }
            ), 
        }
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    widgets = {}