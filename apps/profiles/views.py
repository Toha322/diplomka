from django.shortcuts import render

from .forms import LoginForm, RegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile

def profile_page(request):
    return render(request,'profiles/profile.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    context = {
        'form': form
    }

    return render(request, 'profiles/login.html', context)


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form = form.save()
            profile = UserProfile.objects.create(
                user=form
            )
            profile.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'profiles/registration.html', context)


def user_logout(request):
    logout(request)
    return redirect('index')