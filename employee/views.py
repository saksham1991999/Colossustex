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
from core import models as coremodels

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
        formtitle = 'Profile'
        context = {
            'formtitle':formtitle,
            'form':form,
        }
        return render(request, 'form.html', context)


def EmployeesView(request):
    employees = models.employee.objects.all()
    context = {
        'employees': employees,
    }
    return render(request, 'list_employees.html', context)

def EmployeeAddView(request):
    if request.method == 'POST':
        form = forms.EmployeeProfileForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                                request,
                                'Details Saved Successfully',
                                extra_tags='alert alert-success alert-dismissible fade show'
                            )
        return redirect('employee:employees')
    else:
        form = forms.EmployeeProfileForm()
        formtitle = 'Add Employee Details'
        context = {
            'formtitle':formtitle,
            'form':form,
        }
        return render(request, 'form.html', context)

def EmployeeEditView(request, id):
    employee = models.employee.objects.get(id=id)
    if request.method == 'POST':
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
        return redirect('employee:employees')
    else:
        form = forms.EmployeeProfileForm(instance=employee)
        formtitle = 'Edit Employee Details'
        context = {
            'formtitle':formtitle,
            'form':form,
        }
        return render(request, 'form.html', context)

def EmployeeDeleteView(request, id):
    employee = models.employee.objects.get(id=id)
    employee.delete()
    return redirect('employee:employees')



def SuppliersView(request):
    suppliers = suppliermodels.supplier.objects.all()
    context = {
        'suppliers': suppliers,
    }
    return render(request, 'list_suppliers.html', context)

def SuppliersAddView(request):
    if request.method == 'POST':
        print('POST REQUEST')
        form = forms.SupplierProfileForm(request.POST)
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
        return redirect('employee:suppliers')
    else:
        form = forms.SupplierProfileForm()
        formtitle = 'Add Supplier Details'
        context = {
            'formtitle':formtitle,
            'form':form,
        }
        return render(request, 'form.html', context)

def SupplierEditView(request, id):
    supplier = suppliermodels.supplier.objects.get(id=id)
    if request.method == 'POST':
        print('POST REQUEST')
        form = forms.SupplierProfileForm(request.POST, instance=supplier)
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
        return redirect('employee:suppliers')
    else:
        form = forms.SupplierProfileForm(instance=supplier)
        formtitle = 'Edit Supplier Details'
        context = {
            'formtitle':formtitle,
            'form':form,
        }
        return render(request, 'form.html', context)

def SupplierDeleteView(request, id):
    supplier = suppliermodels.supplier.objects.get(id=id)
    supplier.delete()
    return redirect('employee:suppliers')


def SubAgentView(request):
    agents = agentmodels.agent.objects.all()
    context = {
        'agents': agents,
    }
    return render(request, 'list_sub_agents.html', context)

def SubAgentAddView(request):
    if request.method == 'POST':
        form = forms.SubAgentProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                                request,
                                'Details Saved Successfully',
                                extra_tags='alert alert-success alert-dismissible fade show'
                            )
        return redirect('employee:sub_agents')
    else:
        form = forms.SubAgentProfileForm()
        formtitle = 'Add Sub-Agent Details'
        context = {
            'formtitle':formtitle,
            'form':form,
        }
        return render(request, 'form.html', context)

def SubAgentEditView(request, id):
    agent = agentmodels.agent.objects.get(id = id)
    if request.method == 'POST':
        form = forms.SubAgentProfileForm(request.POST, instance=agent)
        if form.is_valid():
            form.save()
            messages.success(
                                request,
                                'Details Saved Successfully',
                                extra_tags='alert alert-success alert-dismissible fade show'
                            )
        return redirect('employee:sub_agents')
    else:
        form = forms.SubAgentProfileForm(instance=agent)
        formtitle = 'Edit Sub-Agent Details'
        context = {
            'formtitle':formtitle,
            'form':form,
        }
        return render(request, 'form.html', context)

def SubAgentDeleteView(request, id):
    sub_agent = agentmodels.agent.objects.get(id=id)
    sub_agent.delete()
    return redirect('employee:sub_agents')


def BuyersView(request):
    buyers = buyermodels.buyer.objects.all()
    context = {
        'buyers': buyers,
    }
    return render(request, 'list_buyers.html', context)

def BuyersAddView(request):
    if request.method == 'POST':
        form = forms.BuyerProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                                request,
                                'Details Saved Successfully',
                                extra_tags='alert alert-success alert-dismissible fade show'
                            )
        return redirect('employee:buyers')
    else:
        form = forms.BuyerProfileForm()
        formtitle = 'Add Buyer Details'
        context = {
            'formtitle':formtitle,
            'form':form,
        }
        return render(request, 'form.html', context)

def BuyersEditView(request, id):
    buyer = buyermodels.buyer.objects.get(id=id)
    if request.method == 'POST':
        form = forms.BuyerProfileForm(request.POST, instance=buyer)
        if form.is_valid():
            form.save()
            messages.success(
                                request,
                                'Details Saved Successfully',
                                extra_tags='alert alert-success alert-dismissible fade show'
                            )
        return redirect('employee:buyers')
    else:
        form = forms.BuyerProfileForm(instance=buyer)
        formtitle = 'Add Sub-Agent Details'
        context = {
            'formtitle':formtitle,
            'form':form,
        }
        return render(request, 'form.html', context)

def BuyerDeleteView(request, id):
    buyer = buyermodels.buyer.objects.get(id=id)
    buyer.delete()
    return redirect('employee:buyers')


def ProductsView(request):
    products = coremodels.product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'list_products.html', context)

def ProductAddView(request):
    if request.method == 'POST':
        form = forms.ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                                request,
                                'Details Saved Successfully',
                                extra_tags='alert alert-success alert-dismissible fade show'
                            )
        return redirect('employee:products')
    else:
        form = forms.ProductForm()
        formtitle = 'Add Product Details'
        context = {
            'formtitle':formtitle,
            'form':form,
        }
        return render(request, 'form.html', context)

def ProductEditView(request, id):
    product = coremodels.product.objects.get(id=id)
    if request.method == 'POST':
        form = forms.ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(
                                request,
                                'Details Saved Successfully',
                                extra_tags='alert alert-success alert-dismissible fade show'
                            )
        return redirect('employee:products')
    else:
        form = forms.ProductForm(instance=product)
        formtitle = 'Edit Product Details'
        context = {
            'formtitle':formtitle,
            'form':form,
        }
        return render(request, 'form.html', context)

def ProductDeleteView(request, id):
    product = coremodels.product.objects.get(id=id)
    product.delete()
    return redirect('employee:products')


def EnquiriesView(request):
    enquiries = coremodels.order.objects.all()
    context = {
        'enquiries': enquiries,
    }
    return render(request, 'list_buyers.html', context)

def EnquiryAddView(request):
    if request.method == 'POST':
        form = forms.EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                                request,
                                'Details Saved Successfully',
                                extra_tags='alert alert-success alert-dismissible fade show'
                            )
        return redirect('employee:enquiries')
    else:
        form = forms.EnquiryForm()
        formtitle = 'Add Enquiry Details'
        context = {
            'formtitle':formtitle,
            'form':form,
        }
        return render(request, 'form.html', context)

def EnquiryEditView(request, id):
    enquiry = coremodels.order.objects.get(id=id)
    if request.method == 'POST':
        form = forms.ProductForm(request.POST, instance=enquiry)
        if form.is_valid():
            form.save()
            messages.success(
                                request,
                                'Details Saved Successfully',
                                extra_tags='alert alert-success alert-dismissible fade show'
                            )
        return redirect('employee:products')
    else:
        form = forms.ProductForm(instance=enquiry)
        formtitle = 'Edit Enquiry Details'
        context = {
            'formtitle':formtitle,
            'form':form,
        }
        return render(request, 'form.html', context)

def EnquiryDeleteView(request, id):
    enquiry = coremodels.order.objects.get(id=id)
    enquiry.delete()
    return redirect('employee:products')


def BillsView(request):
    bills = coremodels.bill.objects.all()
    context = {
        'bills': bills,
    }
    return render(request, 'list_buyers.html', context)

def BillAddView(request):
    if request.method == 'POST':
        form = forms.BillForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                                request,
                                'Details Saved Successfully',
                                extra_tags='alert alert-success alert-dismissible fade show'
                            )
        return redirect('employee:enquiries')
    else:
        form = forms.BillForm()
        formtitle = 'Add Bill Details'
        context = {
            'formtitle':formtitle,
            'form':form,
        }
        return render(request, 'form.html', context)

def BillEditView(request, id):
    bill = coremodels.bill.objects.get(id=id)
    if request.method == 'POST':
        form = forms.BillForm(request.POST, instance=bill)
        if form.is_valid():
            form.save()
            messages.success(
                                request,
                                'Details Saved Successfully',
                                extra_tags='alert alert-success alert-dismissible fade show'
                            )
        return redirect('employee:bills')
    else:
        form = forms.BillForm(instance=bill)
        formtitle = 'Edit Bill Details'
        context = {
            'formtitle':formtitle,
            'form':form,
        }
        return render(request, 'form.html', context)

def BillDeleteView(request, id):
    bill = coremodels.bill.objects.get(id=id)
    bill.delete()
    return redirect('employee:bills')


def PaymentsView(request):
    payments = coremodels.payment.objects.all()
    context = {
        'payments': payments,
    }
    return render(request, 'list_buyers.html', context)

def PaymentAddView(request):
    if request.method == 'POST':
        form = forms.PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                                request,
                                'Details Saved Successfully',
                                extra_tags='alert alert-success alert-dismissible fade show'
                            )
        return redirect('employee:payments')
    else:
        form = forms.PaymentForm()
        formtitle = 'Add Payment Details'
        context = {
            'formtitle':formtitle,
            'form':form,
        }
        return render(request, 'form.html', context)

def PaymentEditView(request, id):
    payment = coremodels.payment.objects.get(id=id)
    if request.method == 'POST':
        form = forms.PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            messages.success(
                                request,
                                'Details Saved Successfully',
                                extra_tags='alert alert-success alert-dismissible fade show'
                            )
        return redirect('employee:payments')
    else:
        form = forms.PaymentForm(instance=payment)
        formtitle = 'Edit Payment Details'
        context = {
            'formtitle':formtitle,
            'form':form,
        }
        return render(request, 'form.html', context)

def PaymentDeleteView(request, id):
    payment = coremodels.payment.objects.get(id=id)
    payment.delete()
    return redirect('employee:payments')


def ShipmentsView(request):
    shipments = coremodels.shipment.objects.all()
    context = {
        'shipments': shipments,
    }
    return render(request, 'list_buyers.html', context)

def ShipmentAddView(request):
    if request.method == 'POST':
        form = forms.ShipmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                                request,
                                'Details Saved Successfully',
                                extra_tags='alert alert-success alert-dismissible fade show'
                            )
        return redirect('employee:shipments')
    else:
        form = forms.ShipmentForm()
        formtitle = 'Add Shipment Details'
        context = {
            'formtitle':formtitle,
            'form':form,
        }
        return render(request, 'form.html', context)

def ShipmentEditView(request, id):
    shipment = coremodels.shipment.objects.get(id=id)
    if request.method == 'POST':
        form = forms.ShipmentForm(request.POST, instance=shipment)
        if form.is_valid():
            form.save()
            messages.success(
                                request,
                                'Details Saved Successfully',
                                extra_tags='alert alert-success alert-dismissible fade show'
                            )
        return redirect('employee:shipments')
    else:
        form = forms.ShipmentForm(instance=shipment)
        formtitle = 'Edit Shipment Details'
        context = {
            'formtitle':formtitle,
            'form':form,
        }
        return render(request, 'form.html', context)

def ShipmentDeleteView(request, id):
    shipment = coremodels.shipment.objects.get(id=id)
    shipment.delete()
    return redirect('employee:shipments')


