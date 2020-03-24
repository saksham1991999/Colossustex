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

@login_required
def HomeView(request):
    context = {}
    return render(request, 'dashboard.html', context)

@login_required(login_url='/accounts/login/')
def ProfileView(request):
    employee = models.employee.objects.get(user = request.user)
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
            'formtitle':formtitle,
            'form':form,
        }
        return render(request, 'form.html', context)


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
            'formtitle':formtitle,
            'form':form,
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
            'formtitle':formtitle,
            'form':form,
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
            'formtitle':formtitle,
            'form':form,
        }
        return render(request, 'form.html', context)

def SubAgentEditView(request, id):
    agent = agentmodels.agent.objects.get(id = id)
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
            'formtitle':formtitle,
            'form':form,
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
            'formtitle':formtitle,
            'form':form,
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
            'formtitle':formtitle,
            'form':form,
        }
        return render(request, 'form.html', context)

def ProductDeleteView(request, id):
    product = coremodels.product.objects.get(id=id)
    product.delete()
    return redirect('employee:products')

def ProductView(request,id):
    product = coremodels.product.objects.get(id=id)
    context = {
        'product' : product,
    }

    return render(request, 'single_product.html', context)


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
            'formtitle':formtitle,
            'form':form,
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
            'formtitle':formtitle,
            'form':form,
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
            'formtitle':formtitle,
            'form':form,
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
            'formtitle':formtitle,
            'form':form,
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
            'formtitle':formtitle,
            'form':form,
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
            'formtitle':formtitle,
            'form':form,
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
            'formtitle':formtitle,
            'form':form,
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
            'formtitle':formtitle,
            'form':form,
        }
        return render(request, 'form.html', context)

def InspectionsDeleteView(request, id):
    inspection = models.inspection.objects.get(id=id)
    inspection.delete()
    return redirect('employee:inspections')


def SampleRequestsView(request):
    sample_requests = buyermodels.sample_request.objects.all()
    context = {
        'sample_requests': sample_requests,
    }
    return render(request, 'list_enquiry/list_sample_requests.html', context)

def SampleRequestAddView(request):
    if request.method == 'POST':
        form = buyerforms.SampleRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                                request,
                                'Details Saved Successfully',
                                extra_tags='alert alert-success alert-dismissible fade show'
                            )
        return redirect('employee:sample-requests')
    else:
        form = buyerforms.SampleRequestForm()
        formtitle = 'Add Sample Request Details'
        context = {
            'formtitle':formtitle,
            'form':form,
        }
        return render(request, 'form.html', context)

def SampleRequestEditView(request, id):
    sample_request = buyermodels.sample_request.objects.get(id=id)
    if request.method == 'POST':
        form = buyerforms.SampleRequestForm(request.POST, request.FILES, instance=sample_request)
        if form.is_valid():
            form.save()
            messages.success(
                                request,
                                'Details Saved Successfully',
                                extra_tags='alert alert-success alert-dismissible fade show'
                            )
        return redirect('employee:sample-requests')
    else:
        form = buyerforms.SampleRequestForm(instance=sample_request)
        formtitle = 'Edit Sample Request Details'
        context = {
            'formtitle':formtitle,
            'form':form,
        }
        return render(request, 'form.html', context)

def SampleRequestDeleteView(request, id):
    sample_request = buyermodels.sample_request.objects.get(id=id)
    sample_request.delete()
    return redirect('employee:sample-requests')

def VisitNotesView(request):
    employee = models.employee.objects.get(user = request.user)
    notes = models.employee_visit.objects.filter(employee=employee)
    context = {
        'notes': notes,
    }
    return render(request, 'list_others/list_visit_notes.html', context)

def VisitNotesAddView(request):
    if request.method == 'POST':
        employee = models.employee.objects.get(user = request.user)
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
            'formtitle':formtitle,
            'form':form,
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
            'formtitle':formtitle,
            'form':form,
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
            'formtitle':formtitle,
            'form':form,
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
            'formtitle':formtitle,
            'form':form,
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
            'formtitle':formtitle,
            'form':form,
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
            'formtitle':formtitle,
            'form':form,
        }
        return render(request, 'form.html', context)

def UpdatesDeleteView(request, id):
    update = coremodels.updates.objects.get(id=id)
    update.delete()
    return redirect('employee:updates-news')


def LeaveApplicationsView(request):
    employee = models.employee.objects.get(user = request.user)
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
            'formtitle':formtitle,
            'form':form,
        }
        return render(request, 'form.html', context)



###########################################################################################################################
def BuyerComplaintsView(request):
    complaints = buyermodels.buyer_complaints.objects.all()
    context = {
        'complaints': complaints,
    }
    return render(request, 'list_users/list_products.html', context)

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

def BuyerComplaintView(request,id):
    complaint = buyermodels.buyer_complaints.objects.get(id=id)
    context = {
        'complaint': complaint,
    }

    return render(request, 'single_product.html', context)

def SupplierComplaintsView(request):
    complaints = suppliermodels.supplier_complaints.objects.all()
    context = {
        'complaints': complaints,
    }
    return render(request, 'list_users/list_products.html', context)

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

def SupplierComplaintView(request,id):
    complaint = suppliermodels.supplier_complaints.objects.get(id=id)
    context = {
        'complaint': complaint,
    }

    return render(request, 'single_product.html', context)

def SubAgentComplaintsView(request):
    complaints = agentmodels.agent_complaints.objects.all()
    context = {
        'complaints': complaints,
    }
    return render(request, 'list_users/list_products.html', context)

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

def SubAgentComplaintView(request,id):
    complaint = agentmodels.agent_complaints.objects.get(id=id)
    context = {
        'complaint': complaint,
    }
    return render(request, 'single_product.html', context)

def BuyerFeedbacksView(request):
    feedbacks = buyermodels.buyer_general_feedback.objects.all()
    context = {
        'feedbacks': feedbacks,
    }
    return render(request, 'list_users/list_products.html', context)

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
        return redirect('employee:')
    else:
        form = forms.BuyerFeedbackForm()
        formtitle = 'Add Feedback'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def BuyerFeedbackView(request,id):
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
    return render(request, 'list_users/list_products.html', context)

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
        return redirect('employee:')
    else:
        form = forms.SupplierFeedbackForm()
        formtitle = 'Add Feedback'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def SupplierFeedbackView(request,id):
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
    return render(request, 'list_users/list_products.html', context)

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
        return redirect('employee:')
    else:
        form = forms.SubAgentFeedbackForm()
        formtitle = 'Add Feedback'
        context = {
            'formtitle': formtitle,
            'form': form,
        }
        return render(request, 'form.html', context)

def SubAgentFeedbackView(request,id):
    feedback = agentmodels.agent_general_feedback.objects.get(id=id)
    context = {
        'feedback': feedback,
    }
    return render(request, 'single_product.html', context)