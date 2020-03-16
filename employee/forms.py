from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from . import models
from supplier.models import supplier
from agent.models import agent
from buyer.models import buyer
from core import models as coremodels


class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = models.employee
        exclude = ['user']
        labels = {
            'name': _('Full Name')
        }
        # widgets = {
        #     'name': forms.TextInput(attrs={'class':'form-control '}),
        #     'department': forms.Select(attrs={'class':'form-control'}),
        #     'dob': forms.DateInput(attrs={'class':'form-control'}),
        #     'addr1': forms.TextInput(attrs={'class':'form-control'}),
        #     'addr2': forms.TextInput(attrs={'class':'form-control'}),
        #     'state': forms.TextInput(attrs={'class':'form-control'}),
        #     'country': forms.TextInput(attrs={'class':'form-control'}),
        #     'email': forms.EmailInput(attrs={'class':'form-control'}),
        #     'pincode': forms.TextInput(attrs={'class':'form-control', 'pattern': '[0-9]{6}'}),
        #     'mobile': forms.TextInput(attrs={'class':'form-control', 'pattern': '[0-9]{10}'}),
        #     'document': forms.FileInput(attrs={'class':'form-control'}),
        #     'image': forms.FileInput(attrs={'class':'form-control'}),
        # }

class SupplierProfileForm(forms.ModelForm):
    class Meta:
        model = supplier
        exclude = ['user']


class SubAgentProfileForm(forms.ModelForm):
    class Meta:
        model = agent
        exclude = ['user']

class BuyerProfileForm(forms.ModelForm):
    class Meta:
        model = buyer
        exclude = ['user']

class ProductForm(forms.ModelForm):
    class Meta:
        model = coremodels.product
        fields = '__all__'


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = coremodels.order
        fields = '__all__'


class BillForm(forms.ModelForm):
    class Meta:
        model = coremodels.bill
        fields = '__all__'


class PaymentForm(forms.ModelForm):
    class Meta:
        model = coremodels.payment
        fields = '__all__'


class ShipmentForm(forms.ModelForm):
    class Meta:
        model = coremodels.shipment
        fields = '__all__'

