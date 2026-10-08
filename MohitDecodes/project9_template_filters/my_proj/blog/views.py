from django.shortcuts import render
from datetime import datetime

# Create your views here.
def blog_details(request, post_id):
    post = {
        "title": "My Second Template Post", 
        "descriptions": "Django is a high level language which is written in Python.", 
        "author": None,
        "created_at": datetime(2025, 8, 21, 10, 32, 10), 
        "comments_count": 5, 
        "tags": ["Django", "Python", "Web Development"], 
    }
    return render(request, 'blog/blog_details.html', {'post': post})