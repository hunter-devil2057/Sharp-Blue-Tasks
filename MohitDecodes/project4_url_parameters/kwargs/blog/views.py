from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to My Blog Home Page</h1>")

def post_details(request, post_id):
    return HttpResponse(f"<h1>Post Details for Post ID: {post_id}</h1>")

def user_profile(request, username):
    return HttpResponse(f"<h1>Welcome to our Page {username.capitalize()}!<br/> Keep Exploring</h1>")

def article_by_year(request, year):
    return HttpResponse(f"<h1>Article By Year: {year}</h1>")


def article_details(request, year, month, day):
    return HttpResponse(f"<h1>Article By Year: {year}-{month}-{day}</h1>")