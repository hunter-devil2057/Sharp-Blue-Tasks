from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
class User:
    # Creating Constructor
    def __init__(self, name, age):
        self.name = name 
        self.age = age

def home(request):
    # this is api in json form, 
    context = {
        "name": "Manish Shiwakoti", 
        "age": 26, 
        "skill": ["Python", "Django", "React"], 
        "user": User("Anush Shiwakoti", 21), 
        "blog": {
            "title": "<i>Django Templates Introduction</i>", 
            "author": {
                "name": "Ranjan Guragain", 
                "email": "ranjan@gmail.com",
            }, 
            "content": "<b>This is my simple blog post related to Django Templates</b>", 
            "created_at": datetime(2025, 8, 18, 10, 30),    
        }, 
        "empty_value": None, 
    } 
    return render(request, "blog/home.html", context)