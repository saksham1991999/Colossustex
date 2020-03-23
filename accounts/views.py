from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def LoginView(request):
    context = {}
    return render(request, 'login.html', context)


def RegisterView(request):
    context = {}
    return render(request, 'login.html', context)

def LoginView(request):
    logout(request)
    if request.method == 'POST':
        # print('-----------------------------POST REQUEST -----------------------------------')
        # print(request.POST)

        type = request.POST['type']
        email = request.POST['email']
        password = request.POST['password']
        # print(type, email, password)
        if type == 'login':
            user = authenticate(request, username=email, password=password)
            login(request, user)
            if user.is_vendor:
                redirect('vendor:dashboard')
            else:
                return redirect('customer:dashboard')
        elif type == 'register':
            username = request.POST['username'][0]
            user = models.User.objects.create_user(username=email, email=email, password=password)
            user.save()
            user = authenticate(username=email, password=password)
            return redirect('core:home')
        return redirect('core:login')
    else:
        context = {

        }
        return render(request, 'login.html', context)

def LogoutView(request):
    logout(request)
    return redirect('core:home')