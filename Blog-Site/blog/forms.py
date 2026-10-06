from django import forms
from .models import Blog, Comment     # Linking Comments from Model to Form

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment     # kun model ko form ho?
        # k k ko fields/value haru xahinney ho?
        fields = ('name', 'email', 'body')
        # Widgets = Components jasma kun kun attributes haru xahinxa form ma, 
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Name', 'required': True,}), 
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your E-mail Address', 'required': True,}), 
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your Review to Comment this Post......', 'required': True,})
            }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog        # kun model ko form ho? => Blog ko
        fields = ("title", "image", "content", "description", "category")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields["image"].required = False