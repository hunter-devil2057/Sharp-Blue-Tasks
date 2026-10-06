from django import forms
from .models import Blog, Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ("title", "image", "content", "description", "category")
        widgets = {
            'title': forms.TextInput(
                attrs = {
                    'class': 'form-control', 
                    'placeholder': 'Enter Title', 
                    'required': True, 
                }
            ),
            'content': forms.TextInput(
                attrs = {
                    'class': 'form-control', 
                    'placeholder': 'Enter Content', 
                    'required': True, 
                }
            ),
            'description': forms.Textarea(
                attrs = {
                    'class': 'form-control', 
                    'placeholder': 'Enter Description for the Post', 
                    'required': True, 
                }
            ),
        }

        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)

            if self.instance and self.instance.pk:
                self.fields["image"].required = False

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment # kun model ko form ho?
        fields = ('name', 'email', 'body')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Enter your Name', 
                    'required': True
                    }
                ), 
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Enter your Email Address', 
                    'required': True
                    }
                ), 
            'body': forms.Textarea(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Enter your Review to Comment this Post....', 
                    'required': True
                    }
                ), 
        }
