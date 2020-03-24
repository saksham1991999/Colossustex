from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, UserSignupForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from core.models import User

# Create your views here.

def LoginView(request):
    logout(request)
    if request.method == 'GET': #POST
        form = UserLoginForm(request.GET)
        username = request.GET.get('username')
        password = request.GET.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect_url = request.GET.get('next', 'employee:home')
            messages.error(request, 'You\'re logged in as {}'.format(user.username))
            return redirect(redirect_url)
        else:
            messages.error(request, 'Username or Password is Incorrect')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)


def RegisterView(request):
    logout(request)

    if request.method == 'GET':
        form = UserSignupForm(request.GET)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['username']
            user = User.objects.create_user(username,email,password)
            user.save()
            login(request, user)
            redirect_url = request.GET.get('next', 'employee:home')
            messages.error(request, 'You\'re logged in as {}'.format(user.username))
            return redirect(redirect_url)
        else:
            form = UserSignupForm(request.GET)
            messages.error(request, form.errors)
    else:
        form = UserSignupForm()
    context = {'form':form ,}
    return render(request, 'register.html', context)


@login_required
def LogoutView(request):
    logout(request)
    return redirect('core:home')
