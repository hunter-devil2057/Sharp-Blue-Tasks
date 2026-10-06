from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm

# Create your views here.
class Register(View):
    def get(self, request):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, 'Registration Successful!')
                return redirect('dashboard')
            else:
                form = RegisterForm()
                messages.error(request, 'Registration Failed. Please correct the errors below.')
        else:
            form = RegisterForm()
            return render(request, 'accounts/register.html', {'form': form})

class LogIn(View):
    def get(self, request):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login Successful!')
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Invalid username or password.')
        else:
            form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})

class LogOut(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'You have been logged out.')
        return redirect('login')

class Dashboard(View):
    def get(self, request):
        return render(request, 'accounts/dashboard.html')