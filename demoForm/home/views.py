from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required
def index(request):
    return HttpResponse("<h1>Hello, World!</h1>")

@login_required
def dashboard(request):
    return HttpResponse("<h1>Hello, this is Dashboard Page...</h1>")