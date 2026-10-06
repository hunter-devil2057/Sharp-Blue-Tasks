from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required     # login garesi matra dashboard access garna pauni
def dashboard(request):
    return render(request, 'dashboard.html')