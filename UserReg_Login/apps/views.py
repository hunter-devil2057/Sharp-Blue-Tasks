
from django.shortcuts import redirect, render
from django.views import View
from apps.forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


class UserSignUpView(View):
    template_name = 'app/signup.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('apps:profile')
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('apps:profile')
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully!")
            return redirect('apps:login')

        return render(request, self.template_name, {'form': form})


class UserLoginView(View):
    template_name = 'app/userlogin.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('apps:profile')

        form = AuthenticationForm(request)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('apps:profile')

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged In Successfully!")
            return redirect('apps:profile')
        return render(request, self.template_name, {'form': form})


class UserProfileView(View):
    template_name = 'app/profile.html'

    def get(self, request):
        if not request.user.is_authenticated:
            messages.warning(request, "Please log in to access your profile.")
            return redirect('apps:login')

        context = {'name': request.user.first_name}
        return render(request, self.template_name, context)


class UserLogOutView(View):
    def post(self, request):
        logout(request)
        messages.success(request, "Logged Out Successfully!")
        return redirect('apps:login')
