from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import viewsets

from . import models, forms
from supplier import models as suppliermodels
from agent import models as agentmodels
from buyer import models as buyermodels

def HomeView(request):
    context = {}
    return render(request, 'dashboard.html', context)

def ProfileView(request):
    employee = models.employee.objects.get(user = request.user)
    if request.method == 'POST':
        print('POST REQUEST')
        form = forms.EmployeeProfileForm(request.POST, instance=employee)
        print(form.errors)
        if form.is_valid():
            print('FORM IS VALID')
            form.save()
            print('FORM SAVED SUCCESSFULLY')
            messages.success(
                                request,
                                'Details Saved Successfully',
                                extra_tags='alert alert-success alert-dismissible fade show'
                            )
        print('REDIRECTING')
        return redirect('employee:profile')
    else:
        form = forms.EmployeeProfileForm(instance=employee)
        context = {
            'form':form,
        }
        return render(request, 'profile.html', context)

def SuppliersView(request):
    suppliers = suppliermodels.supplier.objects.all()
    context = {
        'suppliers': suppliers,
    }
    return render(request, 'suppliers_list.html', context)


def SupplierDeleteView(request, id):
    supplier = suppliermodels.supplier.objects.get(id=id)
    supplier.delete()
    return redirect('employee:suppliers')

def SubAgentView(request):
    agents = agentmodels.agent.objects.all()
    context = {
        'agents': agents,
    }
    return render(request, 'sub_agents_list.html', context)


def SubAgentDeleteView(request, id):
    sub_agent = agentmodels.agent.objects.get(id=id)
    sub_agent.delete()
    return redirect('employee:sub_agents')

def BuyersView(request):
    buyers = buyermodels.buyer.objects.all()
    context = {
        'buyers': buyers,
    }
    return render(request, 'buyers_list.html', context)


def BuyerDeleteView(request, id):
    buyer = buyermodels.buyer.objects.get(id=id)
    buyer.delete()
    return redirect('employee:buyers')

# def ContactView(request):
#     if request.method == 'POST':
#         form = forms.ContactForm(request.POST)
#         print(request.POST)
#         if form.is_valid():
#             form.save()
#             print('Form saved Successfully')
#             messages.success(
#                 request,
#                 'Message sent Successfully',
#                 extra_tags='alert alert-success alert-dismissible fade show'
#             )
#         else:
#             print(form.errors)
#             print('form not valid')
#         return redirect('core:contact')
#     else:
#         form = forms.ContactForm()
#         context = {
#             'contactform': form,
#         }
#         return render(request, 'contact.html', context)
