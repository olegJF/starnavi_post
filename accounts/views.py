from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views.generic.edit import FormView
from django.contrib.auth import (login, logout, authenticate)
from .forms import SignUpForm, UserLoginForm

User = get_user_model()

class UserSignUpView(FormView):
    template_name = 'accounts/sign_up.html'
    form_class = SignUpForm
    success_url = '/login'

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create(username=username, email=email)
        new_user.set_password(password)
        new_user.save()
        return super(UserSignUpView, self).form_valid(form)
        
def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(email=email, password=password)
        login(request, user)
        return redirect('home')
    
    return render(request, 'accounts/login.html', {"form": form,})


def logout_view(request):
    logout(request)

    return redirect('home')