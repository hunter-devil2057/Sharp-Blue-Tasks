from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def shop_home(request):
    return HttpResponse("<h1>This is Shop Home Page</h1>")

def shop_product(request):
    return HttpResponse("<h1>This is Shop Product Page</h1>")