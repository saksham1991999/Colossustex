from django.forms import inlineformset_factory, modelformset_factory
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
from buyer import forms as buyerforms
from core import models as coremodels
from hr import models as hrmodels

import datetime

def TestView(request):
    context = {
        'tests': [1, 2, 3, 4, 5]
    }
    return render(request, 'list_others/updates_news.html', context)

@login_required
def HomeView(request):
    context = {}
    return render(request, 'dashboard.html', context)

@login_required(login_url='/accounts/login/')
def ProfileView(request):
    employee = models.employee.objects.get(user=request.user)
    if request.method == 'POST':
        print('POST REQUEST')
        form = forms.EmployeeProfileForm(request.POST, request.FILES, instance=employee)
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
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

#EMPLOYEE VIEWS
def EmployeesView(request):
    employees = models.employee.objects.all()
    context = {
        'employees': employees,
    }
    return render(request, 'list_users/list_employees.html', context)

def EmployeeAddView(request):
    if request.method == 'POST':
        form = forms.EmployeeProfileForm(request.POST, request.FILES)

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
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def EmployeeEditView(request, id):
    employee = models.employee.objects.get(id=id)
    if request.method == 'POST':
        form = forms.EmployeeProfileForm(request.POST, request.FILES, instance=employee)
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
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def EmployeeViewView(request, id):
    employee = models.employee.objects.get(id=id)
    context = {
        'employee': employee,
    }
    return render(request, 'list_users/single_employee.html', context)

def EmployeeDeleteView(request, id):
    employee = models.employee.objects.get(id=id)
    employee.delete()
    return redirect('employee:employees')

#SUPPLIER VIEWS
def SuppliersView(request):
    suppliers = suppliermodels.supplier.objects.all()
    context = {
        'suppliers': suppliers,
    }
    return render(request, 'list_users/list_suppliers.html', context)

def SuppliersAddView(request):
    if request.method == 'POST':
        print('POST REQUEST')
        form = forms.SupplierProfileForm(request.POST, request.FILES)
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
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def SupplierEditView(request, id):
    supplier = suppliermodels.supplier.objects.get(id=id)
    if request.method == 'POST':
        print('POST REQUEST')
        form = forms.SupplierProfileForm(request.POST, request.FILES, instance=supplier)
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
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def SupplierViewView(request, id):
    supplier = suppliermodels.supplier.objects.get(id=id)
    context = {
        'supplier': supplier,
    }
    return render(request, 'list_users/single_supplier.html', context)

def SupplierDeleteView(request, id):
    supplier = suppliermodels.supplier.objects.get(id=id)
    supplier.delete()
    return redirect('employee:suppliers')

#SUB-AGENT VIEWS
def SubAgentView(request):
    agents = agentmodels.agent.objects.all()
    context = {
        'agents': agents,
    }
    return render(request, 'list_users/list_sub_agents.html', context)

def SubAgentAddView(request):
    if request.method == 'POST':
        form = forms.SubAgentProfileForm(request.POST, request.FILES)
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
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def SubAgentEditView(request, id):
    agent = agentmodels.agent.objects.get(id=id)
    if request.method == 'POST':
        form = forms.SubAgentProfileForm(request.POST, request.FILES, instance=agent)
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
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def SubAgentViewView(request, id):
    agent = agentmodels.agent.objects.get(id=id)
    context = {
        'agent': agent,
    }
    return render(request, 'list_users/single_agent.html', context)

def SubAgentDeleteView(request, id):
    sub_agent = agentmodels.agent.objects.get(id=id)
    sub_agent.delete()
    return redirect('employee:sub_agents')

#BUYER VIEWS
def BuyersView(request):
    buyers = buyermodels.buyer.objects.all()
    context = {
        'buyers': buyers,
    }
    return render(request, 'list_users/list_buyers.html', context)

def BuyersAddView(request):
    if request.method == 'POST':
        form = forms.BuyerProfileForm(request.POST, request.FILES)
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
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def BuyersEditView(request, id):
    buyer = buyermodels.buyer.objects.get(id=id)
    if request.method == 'POST':
        form = forms.BuyerProfileForm(request.POST, request.FILES, instance=buyer)
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
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def BuyersViewView(request, id):
    buyer = buyermodels.buyer.objects.get(id=id)

    context = {
        'buyer': buyer,
    }
    return render(request, 'list_users/single_buyer.html', context)

def BuyerDeleteView(request, id):
    buyer = buyermodels.buyer.objects.get(id=id)
    buyer.delete()
    return redirect('employee:buyers')

#PRODUCT VIEWS
def ProductsView(request):
    products = coremodels.product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'list_users/list_products.html', context)

def ProductAddView(request):
    if request.method == 'POST':
        form = forms.ProductForm(request.POST, request.FILES)
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
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def ProductEditView(request, id):
    product = coremodels.product.objects.get(id=id)
    if request.method == 'POST':
        form = forms.ProductForm(request.POST, request.FILES, instance=product)
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
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def ProductDeleteView(request, id):
    product = coremodels.product.objects.get(id=id)
    product.delete()
    return redirect('employee:products')

def ProductView(request, id):
    product = coremodels.product.objects.get(id=id)
    context = {
        'product': product,
    }

    return render(request, 'list_users/single_product.html', context)







def EnquiriesView(request):
    enquiries = coremodels.order.objects.all()
    context = {
        'enquiries': enquiries,
    }
    return render(request, 'list_enquiry/list_enquiries.html', context)

def EnquiryAddView(request):
    if request.method == 'POST':
        form = forms.EnquiryForm(request.POST, request.FILES)
        if form.is_valid():
            print('Adding Enquiry')
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
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def EnquiryEditView(request, id):
    enquiry = coremodels.order.objects.get(id=id)
    if request.method == 'POST':
        form = forms.ProductForm(request.POST, request.FILES, instance=enquiry)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Details Saved Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
        return redirect('employee:enquiries')
    else:
        form = forms.ProductForm(instance=enquiry)
        formtitle = 'Edit Enquiry Details'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def EnquiryDeleteView(request, id):
    enquiry = coremodels.order.objects.get(id=id)
    enquiry.delete()
    return redirect('employee:enquiries')

def BillsView(request):
    bills = coremodels.bill.objects.all()
    context = {
        'bills': bills,
    }
    return render(request, 'list_enquiry/list_bills.html', context)

def BillAddView(request):
    if request.method == 'POST':
        form = forms.BillForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Details Saved Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
        return redirect('employee:bills')
    else:
        form = forms.BillForm()
        formtitle = 'Add Bill Details'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def BillEditView(request, id):
    bill = coremodels.bill.objects.get(id=id)
    if request.method == 'POST':
        form = forms.BillForm(request.POST, request.FILES, instance=bill)
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
            'formtitle': formtitle,
            'form': form,
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
    return render(request, 'list_enquiry/list_payments.html', context)

def PaymentAddView(request):
    if request.method == 'POST':
        form = forms.PaymentForm(request.POST, request.FILES)
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
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def PaymentEditView(request, id):
    payment = coremodels.payment.objects.get(id=id)
    if request.method == 'POST':
        form = forms.PaymentForm(request.POST, request.FILES, instance=payment)
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
            'formtitle': formtitle,
            'form': form,
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
    return render(request, 'list_enquiry/list_shipment.html', context)

def ShipmentAddView(request):
    if request.method == 'POST':
        form = forms.ShipmentForm(request.POST, request.FILES)
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
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def ShipmentEditView(request, id):
    shipment = coremodels.shipment.objects.get(id=id)
    if request.method == 'POST':
        form = forms.ShipmentForm(request.POST, request.FILES, instance=shipment)
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
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def ShipmentDeleteView(request, id):
    shipment = coremodels.shipment.objects.get(id=id)
    shipment.delete()
    return redirect('employee:shipments')

def InspectionsView(request):
    inspections = models.inspection.objects.all()
    context = {
        'inspections': inspections,
    }
    return render(request, 'list_enquiry/list_shipment.html', context)

def InspectionsAddView(request):
    if request.method == 'POST':
        form = forms.InspectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Details Saved Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
        return redirect('employee:inspections')
    else:
        form = forms.ShipmentForm()
        formtitle = 'Add Inspection Details'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def InspectionsEditView(request, id):
    inspection = models.inspection.objects.get(id=id)
    if request.method == 'POST':
        form = forms.InspectionForm(request.POST, request.FILES, instance=inspection)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Details Saved Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
        return redirect('employee:inspections')
    else:
        form = forms.InspectionForm(instance=inspection)
        formtitle = 'Edit Inspection Details'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def InspectionsDeleteView(request, id):
    inspection = models.inspection.objects.get(id=id)
    inspection.delete()
    return redirect('employee:inspections')


def VisitNotesView(request):
    employee = models.employee.objects.get(user=request.user)
    notes = models.employee_visit.objects.filter(employee=employee)
    context = {
        'notes': notes,
    }
    return render(request, 'list_others/list_visit_notes.html', context)

def VisitNotesAddView(request):
    if request.method == 'POST':
        employee = models.employee.objects.get(user=request.user)
        form = forms.VisitNoteForm(request.POST, request.FILES)
        print(employee)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.employee = employee
            new_form.save()
            messages.success(
                request,
                'Details Saved Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
        return redirect('employee:visit-notes')
    else:
        form = forms.VisitNoteForm()
        formtitle = 'Add Visit Notes'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def VisitNotesEditView(request, id):
    note = models.employee_visit.objects.get(id=id)
    if request.method == 'POST':
        form = forms.VisitNoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Details Saved Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
        return redirect('employee:visit-notes')
    else:
        form = forms.VisitNoteForm(instance=note)
        formtitle = 'Edit Visit Note'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def VisitNotesDeleteView(request, id):
    note = models.employee_visit.objects.get(id=id)
    note.delete()
    return redirect('employee:visit-notes')

def SuplusProductsView(request):
    suplus_products = coremodels.suplus_product.objects.all()
    context = {
        'suplus_products': suplus_products,
    }
    return render(request, 'list_others/list_suplus_products.html', context)

def SuplusProductsAddView(request):
    if request.method == 'POST':
        form = forms.SuplusProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Details Saved Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
        return redirect('employee:suplus-products')
    else:
        form = forms.SuplusProductForm()
        formtitle = 'Add Suplus Product Details'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def SuplusProductsEditView(request, id):
    suplus_product = coremodels.suplus_product.objects.get(id=id)
    if request.method == 'POST':
        form = forms.SuplusProductForm(request.POST, request.FILES, instance=suplus_product)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Details Saved Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
        return redirect('employee:suplus-products')
    else:
        form = forms.SuplusProductForm(instance=suplus_product)
        formtitle = 'Edit Suplus Product Details'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def SuplusProductsDeleteView(request, id):
    suplus_product = coremodels.suplus_product.objects.get(id=id)
    suplus_product.delete()
    return redirect('employee:suplus-products')

def UpdatesView(request):
    updates = coremodels.suplus_product.objects.all()
    context = {
        'updates': updates,
    }
    return render(request, 'list_others/list_updates.html', context)

def UpdatesAddView(request):
    if request.method == 'POST':
        form = forms.UpdateNewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Details Saved Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
        return redirect('employee:updates-news')
    else:
        form = forms.UpdateNewsForm()
        formtitle = 'Add Update/News'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def UpdatesEditView(request, id):
    update = coremodels.updates.objects.get(id=id)
    if request.method == 'POST':
        form = forms.UpdateNewsForm(request.POST, request.FILES, instance=update)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Details Saved Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
        return redirect('employee:updates-news')
    else:
        form = forms.UpdateNewsForm(instance=update)
        formtitle = 'Edit Update/News'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def UpdatesDeleteView(request, id):
    update = coremodels.updates.objects.get(id=id)
    update.delete()
    return redirect('employee:updates-news')

def LeaveApplicationsView(request):
    employee = models.employee.objects.get(user=request.user)
    applications = hrmodels.leaveapplication.objects.filter(employee=employee)

    context = {
        'applications': applications,
    }
    return render(request, 'list_others/list_leave_applications.html', context)

def SubmitLeaveApplicationView(request):
    if request.method == 'POST':
        employee = models.employee.objects.get(user=request.user)
        form = forms.LeaveApplicationEmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Details Saved Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
        return redirect('employee:updates-news')
    else:
        form = forms.LeaveApplicationEmployeeForm()
        formtitle = 'Submit A new Leave Application'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

# INQUIRY MANAGEMENT VIEWS
@login_required(login_url='/accounts/login/')
def InquiresView(request):
    inquiries = coremodels.inquiry.objects.all()
    context = {
        'inquiries': inquiries,
    }
    return render(request, 'list_inquiry/list_inquiries.html', context)

@login_required(login_url='/accounts/login/')
def InquiryView(request, id):
    inquiry = coremodels.inquiry.objects.get(id=id)
    context = {
        'inquiry': inquiry,
    }
    return render(request, 'list_inquiry/inquiry.html', context)

@login_required(login_url='/accounts/login/')
def AddInquiryView(request):
    if request.method == 'POST':
        form = forms.InquiryForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.received_datetime = datetime.datetime.now()
            new_form.save()
            messages.success(
                request,
                'Inquiry Saved Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
            return redirect('employee:inquiry_add_product', new_form.id)
        return redirect('employee:add_inquiry')
    else:
        form = forms.InquiryForm()
        formtitle = 'Add Inquiry Details'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'list_inquiry/add_inquiry.html', context)

def AddInquiryProductView(request, id):
    inquiry = coremodels.inquiry.objects.get(id=id)
    InquiryProductFormSet = inlineformset_factory(coremodels.inquiry, coremodels.inquiry_product, exclude=('inquiry', 'suppliers'),
                                                  can_delete=False, extra=1)

    if request.method == 'POST':
        formset = InquiryProductFormSet(request.POST, instance=inquiry, prefix='Product', )
        if formset.is_valid():
            formset.save()
            messages.success(
                request,
                'Product Details Added Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
        return redirect('employee:inquiry', id)
    else:
        formset = InquiryProductFormSet(prefix='Product', instance=inquiry)
        formtitle = 'Add Inquiry Product Details'
        context = {
            'formtitle': formtitle,
            'formset': formset,
        }
        return render(request, 'list_inquiry/AddProductInquiry_formset.html', context)

def EditInquiryProductView(request, id):
    inquiry_product = coremodels.inquiry_product.objects.get(id=id)
    if request.method == 'POST':
        form = forms.InquiryProductForm(request.POST, request.FILES, instance=inquiry_product)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Product Details Added Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
        return redirect('employee:inquiry', inquiry_product.inquiry.id)
    else:
        form = forms.InquiryProductForm(instance=inquiry_product)
        formtitle = 'Edit Inquiry Product Details'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def DeleteInquiryProductView(request, id):
    inquiry_product = coremodels.inquiry_product.objects.get(id=id)
    inquiry_id = inquiry_product.inquiry.id
    inquiry_product.delete()
    return redirect('employee:inquiry', inquiry_id)

def InquiryNotifySuppliersView(request, id):
    inquiry = coremodels.inquiry.objects.get(id=id)

    if request.method == 'POST':
        print(request.POST)
        total_forms = request.POST["total-forms"]
        for formidx in range(int(total_forms)):
            inquiry_product_id_str = "inquiry-product-id-"+str(formidx)
            inquiry_product_suppliers_str = "inquiry-product-suppliers-"+str(formidx)
            inquiry_product_id = request.POST[inquiry_product_id_str]
            inquiry_product_suppliers = request.POST.getlist(inquiry_product_suppliers_str)

            inquiry_product = coremodels.inquiry_product.objects.get(id=inquiry_product_id)
            inquiry_product.suppliers.clear()
            for supplier_id in inquiry_product_suppliers:
                supplier = suppliermodels.supplier.objects.get(id=supplier_id)
                inquiry_product.suppliers.add(supplier)
            inquiry_product.save()
        inquiry.reply_datetime = datetime.datetime.now()
        return redirect('employee:inquiry', id)
    else:
        formtitle = 'Select Suppliers'
        InquiryProducts = coremodels.inquiry_product.objects.filter(inquiry = inquiry)
        context = {
            'formtitle': formtitle,
            'InquiryProducts': InquiryProducts,
        }
        return render(request, 'list_inquiry/SelectProductSuppliers_formset.html', context)

def AddSupplierQuotationView(request, id):
    inquiry = coremodels.inquiry.objects.get(id=id)
    SupplierFormSet = inlineformset_factory(coremodels.inquiry, coremodels.supplier_quotations, exclude=('inquiry',),
                                            can_delete=False, extra=1)

    if request.method == 'POST':
        formset = SupplierFormSet(request.POST, instance=inquiry, prefix='quotation')
        if formset and formset.is_valid():
            formset.save()
            messages.success(
                request,
                'Quotation Details Added Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
            return redirect('employee:inquiry', id)
    else:
        formset = SupplierFormSet(instance=inquiry, prefix='quotation')
        formtitle = 'Add Inquiry Product Details'
        context = {
            'formtitle': formtitle,
            'formset': formset,
        }
        return render(request, 'list_inquiry/AddSupplierQuotation_formset.html', context)

def AddSupplierQuotationView2(request, id):
    inquiry = coremodels.inquiry.objects.get(id=id)
    inquiry_products = coremodels.inquiry_product.objects.filter(inquiry=inquiry)

    if request.method == 'POST':
        print(request.POST)
        total_products = request.POST['total_products']
        print(total_products)
        for product_idx in range(1, int(total_products)+1):
            total_forms = request.POST['total_forms_product_'+str(product_idx)]
            inquiry_product_id = request.POST['inquiry_product_id_'+str(product_idx)]
            inquiry_product = coremodels.inquiry_product.objects.get(id = inquiry_product_id)
            print(inquiry_product)
            for form_idx in range(int(total_forms)):
                try:
                    supplier_str = 'supplier_' + str(product_idx) + '_form_' + str(form_idx)
                    price_kg_str = 'price_kg_' + str(product_idx) + '_form_' + str(form_idx)
                    payment_terms_str = 'payment_term_' + str(product_idx) + '_form_' + str(form_idx)

                    supplier_id = request.POST[supplier_str]
                    supplier = coremodels.supplier.objects.get(id=supplier_id)
                    price_kg = request.POST[price_kg_str]
                    payment_terms = request.POST[payment_terms_str]
                    print("##########################################################################")
                    quotation = coremodels.supplier_quotations.objects.create(inquiry = inquiry,
                                                                              product = inquiry_product,
                                                                              price_kg = price_kg,
                                                                              payment_terms_id = payment_terms,
                                                                              supplier=supplier
                                                                              )
                    quotation.save()
                    print(str(product_idx) + '_form_' + str(form_idx) + ' Save Successfully')
                except:
                    pass
        inquiry.received_quotation_datetime = datetime.datetime.now()
        return redirect('employee:inquiry' , inquiry.id)
    else:
        paymentterms = coremodels.PaymentTerms.objects.all()
        formtitle = 'Add Inquiry Product Details'
        context = {
            'formtitle': formtitle,
            'inquiry_products': inquiry_products,
            'paymentterms': paymentterms,
        }
        return render(request, 'list_inquiry/AddSupplierQuotation_formset2.html', context)

def SelectForwardQuotationsView(request, id):
    if request.method == 'POST':
        form = forms.ForwardedQuotationsForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            inquiry = coremodels.inquiry.objects.get(id=id)
            inquiry.selected_quotation_datetime = datetime.datetime.now()
            inquiry.save()
            new_form.inquiry = inquiry
            new_form.save()
            form.save_m2m()
            messages.success(
                request,
                'Quotations Selected Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
        return redirect('employee:inquiry', id)
    else:
        form = forms.ForwardedQuotationsForm()
        inquiry = coremodels.inquiry.objects.get(id=id)
        form.fields['quotations'].queryset = coremodels.supplier_quotations.objects.filter(inquiry=inquiry)
        formtitle = 'Select Quotations Forwarded'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def AddInquiryUpdateView(request, id):
    if request.method == 'POST':
        form = forms.InquiryUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            inquiry = coremodels.inquiry.objects.get(id=id)
            inquiry.customer_feedback_datetime = datetime.datetime.now()
            inquiry.save()
            new_form.inquiry = inquiry
            new_form.save()
            messages.success(
                request,
                'Update Successfully Added',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
        return redirect('employee:inquiry', id)
    else:
        form = forms.InquiryUpdateForm()
        formtitle = 'Add Updates'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def CloseInquiryView(request, id):
    inquiry = coremodels.inquiry.objects.get(id=id)
    if request.method == 'POST':
        form = forms.ClosingInquiryForm(request.POST, request.FILES, instance=inquiry)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.status = 'CD'
            employee = models.employee.objects.get(user=request.user)
            new_form.confirming_user = employee
            inquiry.confirmation_datetime = datetime.datetime.now()
            new_form.save()
        return redirect('employee:inquiry', id)
    else:
        form = forms.ClosingInquiryForm(instance=inquiry)
        formtitle = 'Closing Inquiry Reason'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def ConfirmInquiryView(request, id):
    print('----------------CONFIRMED INQUIRY------------------')
    inquiry = coremodels.inquiry.objects.get(id=id)
    inquiry.status = 'CM'
    employee = models.employee.objects.get(user=request.user)
    inquiry.confirming_user = employee
    inquiry.confirmation_datetime = datetime.datetime.now()
    inquiry.save()
    return redirect('employee:inquiry', id)

#SAMPLE REQUEST MANAGEMENT
def SampleRequestsView(request):
    sample_requests = coremodels.SampleRequest.objects.all()
    context = {
        'sample_requests': sample_requests,
    }
    return render(request, 'list_sample_request/list_sample_requests.html', context)

def SampleRequestView(request, id):
    sample_request = coremodels.SampleRequest.objects.get(id = id)
    context = {
        'sample_request': sample_request,
    }
    return render(request, 'list_sample_request/sample_request.html', context)

def AddSampleRequest(request):
    if request.method == 'POST':
        form = forms.SampleRequestForm(request.POST,request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            form.save()
            messages.success(
                request,
                'Sample Request Saved Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
            return redirect('employee:sample_request_add_product', new_form.id)
    else:
        form = forms.SampleRequestForm()
        formtitle = 'Add Sample Request'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'list_sample_request/add_sample_request.html', context)

def AddSampleRequestProduct(request, id):
    sample_request = coremodels.SampleRequest.objects.get(id=id)
    SampleRequestProductFormset = inlineformset_factory(coremodels.SampleRequest, coremodels.SampleRequestProduct,can_delete=False, extra=1, fields='__all__')
    # SampleRequestProductFormset = modelformset_factory(coremodels.SampleRequestProduct, extra=4, exclude=('sample_request',))

    if request.method == 'POST':
        formset = SampleRequestProductFormset(request.POST, instance=sample_request , prefix= 'sample_request')
        if formset.is_valid():
            formset.save()
            messages.success(
                request,
                'Product Details Added Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
            return redirect('employee:sample_request', id)
    else:
        formset = SampleRequestProductFormset(prefix='sample_request', instance=sample_request)
        formtitle = 'Add Inquiry Product Details'
        context = {
            'formtitle': formtitle,
            'formset': formset,
        }
        return render(request, 'list_sample_request/SampleRequestProduct_formset.html', context)

def AddCustomerSampleRef(request, id):
    sample_request = coremodels.SampleRequest.objects.get(id=id)
    CustomerSampleRefFormset = inlineformset_factory(coremodels.SampleRequest, coremodels.CustomerSampleRef,
                                                        extra=1, exclude=('id',))

    if request.method == 'POST':
        formset = CustomerSampleRefFormset(request.POST, request.FILES, instance = sample_request, prefix = 'customer_sample')
        if formset.is_valid():
            formset.save()
            messages.success(
                request,
                'Customer Sample Referencce Details Saved Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
            return redirect('employee:sample_request', id)
    else:
        formset = CustomerSampleRefFormset(instance = sample_request, prefix = 'customer_sample')
        formtitle = 'Add Customer Sample Reference Details'
        context = {
            'formtitle': formtitle,
            'formset': formset,
        }
        return render(request, 'list_sample_request/SampleRequestCustomerSampleReference_formset.html', context)

def AddSampleRequestDispatch(request, id):
    sample_request = coremodels.SampleRequest.objects.get(id=id)
    if request.method == 'POST':
        form = forms.SampleRequestDispatchForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.sample_request = sample_request
            new_form.save()
            messages.success(
                request,
                'Sample Request Dispacth Details Saved Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
        return redirect('employee:sample_request', id)
    else:
        form = forms.SampleRequestDispatchForm()
        formtitle = 'Add Sample Request Dispatch Details'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def AddSampleRequestFeedback(request, id):
    sample_request = coremodels.SampleRequest.objects.get(id=id)
    if request.method == 'POST':
        form = forms.SampleRequestFeedbackForm(request.POST,request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.sample_request = sample_request
            new_form.save()
            messages.success(
                request,
                'Sample Request Feedback Saved Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
        return redirect('employee:sample_request', id)
    else:
        form = forms.SampleRequestFeedbackForm()
        formtitle = 'Add Sample Request Feedback'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def SampleRequestUpdateDeliveryDate(request, id):
    sample_request = coremodels.SampleRequest.objects.get(id=id)
    sample_request.delivered_date = datetime.date.today()
    sample_request.save()
    return redirect('employee:sample_request', id)

def SampleRequestUpdateFeedback(request,id):
    sample_request = coremodels.SampleRequest.objects.get(id=id)
    if request.method == 'POST':
        form = forms.SampleRequestFeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.sample_request = sample_request
            new_form.save()
            messages.success(
                request,
                'Feedback Saved Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
        return redirect('employee:sample_request', id)
    else:
        form = forms.SampleRequestFeedbackForm()
        formtitle = 'Edit Feedback Details'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

###########################################################################################################################
def BuyerComplaintsView(request):
    if request.method == 'POST':
        print(request.POST)
        complaint_id = int(request.POST['complaint_id'])
        message = request.POST['message']
        response = buyermodels.complaint_response.objects.create(complaint_id=complaint_id, message=message,
                                                                 user=request.user)
        response.save()
        return redirect('core:buyer_complaints')
    else:
        complaints = buyermodels.buyer_complaints.objects.all()
        context = {
            'complaints': complaints,
        }
        return render(request, 'complaints_management/buyer_complaints.html', context)

def BuyerComplaintAddView(request):
    if request.method == 'POST':
        form = forms.BuyerComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Complaint Saved Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
        return redirect('employee:')
    else:
        form = forms.BuyerComplaintForm()
        formtitle = 'Add Complaint'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def BuyerComplaintAddResponseView(request, id):
    if request.method == 'POST':
        message = request.POST['message']
        response = buyermodels.complaint_response.objects.create(complaint_id=id, message=message,
                                                                 user=request.user)
        response.save()
        return redirect('employee:buyer_complaints')
    else:
        return redirect('employee:buyer_complaints')

def SupplierComplaintsView(request):
    if request.method == 'POST':
        complaint_id = request.POST['complaint_id']
        message = request.POST['message']
        response = suppliermodels.complaint_response.objects.create(complaint_id=complaint_id, message=message,
                                                                    user=request.user)
        response.save()
        return redirect('core:buyer_complaints')
    else:
        complaints = suppliermodels.supplier_complaints.objects.all()
        context = {
            'complaints': complaints,
        }
        return render(request, 'complaints_management/supplier_complaints.html', context)

def SupplierComplaintAddView(request):
    if request.method == 'POST':
        form = forms.SupplierComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Complaint Saved Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
        return redirect('employee:')
    else:
        form = forms.SupplierComplaintForm()
        formtitle = 'Add Complaint'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def SupplierComplaintAddResponseView(request, id):
    if request.method == 'POST':
        message = request.POST['message']
        response = buyermodels.complaint_response.objects.create(complaint_id=id, message=message,
                                                                 user=request.user)
        response.save()
        return redirect('employee:supplier_complaints')
    else:
        return redirect('employee:supplier_complaints')

def SubAgentComplaintsView(request):
    if request.method == 'POST':
        complaint_id = request.POST['complaint_id']
        message = request.POST['message']
        response = suppliermodels.complaint_response.objects.create(complaint_id=complaint_id, message=message,
                                                                    user=request.user)
        response.save()
        return redirect('core:buyer_complaints')
    else:
        complaints = agentmodels.agent_complaints.objects.all()
        context = {
            'complaints': complaints,
        }
        return render(request, 'complaints_management/sub_agent_complaint.html', context)

def SubAgentComplaintAddView(request):
    if request.method == 'POST':
        form = forms.SubAgentComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Complaint Saved Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
        return redirect('employee:')
    else:
        form = forms.SubAgentComplaintForm()
        formtitle = 'Add Complaint'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def SubAgentComplaintAddResponseView(request, id):
    if request.method == 'POST':
        message = request.POST['message']
        response = buyermodels.complaint_response.objects.create(complaint_id=id, message=message,
                                                                 user=request.user)
        response.save()
        return redirect('employee:sub_agent_complaints')
    else:
        return redirect('employee:sub_agent_complaints')

def BuyerFeedbacksView(request):
    feedbacks = buyermodels.buyer_general_feedback.objects.all()
    context = {
        'feedbacks': feedbacks,
    }
    return render(request, 'feedbacks/buyer_feedbacks.html', context)

def BuyerFedbackAddView(request):
    if request.method == 'POST':
        form = forms.BuyerFeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Feedback Saved Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
        return redirect('employee:buyer_feedbacks')
    else:
        form = forms.BuyerFeedbackForm()
        formtitle = 'Add Feedback'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def BuyerFeedbackView(request, id):
    feedback = buyermodels.buyer_general_feedback.objects.get(id=id)
    context = {
        'feedback': feedback,
    }
    return render(request, 'single_product.html', context)

def SupplierFeedbacksView(request):
    feedbacks = suppliermodels.supplier_feedback.objects.all()
    context = {
        'feedbacks': feedbacks,
    }
    return render(request, 'feedbacks/supplier_feedbacks.html', context)

def SupplierFedbackAddView(request):
    if request.method == 'POST':
        form = forms.SupplierFeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Feedback Saved Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
        return redirect('employee:supplier_feedbacks')
    else:
        form = forms.SupplierFeedbackForm()
        formtitle = 'Add Feedback'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def SupplierFeedbackView(request, id):
    feedback = suppliermodels.supplier_feedback.objects.get(id=id)
    context = {
        'feedback': feedback,
    }
    return render(request, 'single_product.html', context)

def SubAgentFeedbacksView(request):
    feedbacks = agentmodels.agent_general_feedback.objects.all()
    context = {
        'feedbacks': feedbacks,
    }
    return render(request, 'feedbacks/sub_agent_feedbacks.html', context)

def SubAgentFedbackAddView(request):
    if request.method == 'POST':
        form = forms.SubAgentFeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Feedback Saved Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
        return redirect('employee:sub_agent_feedbacks')
    else:
        form = forms.SubAgentFeedbackForm()
        formtitle = 'Add Feedback'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def SubAgentFeedbackView(request, id):
    feedback = agentmodels.agent_general_feedback.objects.get(id=id)
    context = {
        'feedback': feedback,
    }
    return render(request, 'single_product.html', context)



