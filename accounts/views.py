from django.shortcuts import render

# Create your views here.

def LoginView(request):
    context = {}
    return render(request, 'login.html', context)


def RegisterView(request):
    context = {}
    return render(request, 'login.html', context)

