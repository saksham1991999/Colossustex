from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from . import models

class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = models.employee
        exclude = ['user']
        labels = {
            'name': _('Full Name')
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control '}),
            'department': forms.Select(attrs={'class':'form-control'}),
            'dob': forms.DateInput(attrs={'class':'form-control'}),
            'addr1': forms.TextInput(attrs={'class':'form-control'}),
            'addr2': forms.TextInput(attrs={'class':'form-control'}),
            'state': forms.TextInput(attrs={'class':'form-control'}),
            'country': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'pincode': forms.TextInput(attrs={'class':'form-control', 'pattern': '[0-9]{6}'}),
            'mobile': forms.TextInput(attrs={'class':'form-control', 'pattern': '[0-9]{10}'}),
            'document': forms.FileInput(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),

        }

# class LibraryForm(forms.ModelForm):
    # class Meta:
    #     model = models.library
    #     exclude = ['owner', 'verified','visible','views']
        # labels = {
        #     'type': _('Select Type'),
        #     'property_name': _('Property Name'),
        #     'city': _('City'),
        #     'bedrooms': _('No of Bedrooms'),
        #     'bathrooms': _('No of Bathrooms'),
        #     'rooms': _('No of Rooms'),
        #     'construction_status': _('Construction Status (Optional)'),
        #     'available_from': _('Available from Date (YYYY-MM-DD) (Optional)'),
        #     'price_sq': _('Price per sq m (Optional)'),
        #     'total_price': _('Total Price'),
        #     'additional_features': _('Additional Features'),
        #     'image': _('Main Image'),
        #     'label': _('Label (Optional)'),
        #     'features': _('Features (Multi-Select)'),
        # }
        # widgets = {
        #     'opening_time': forms.TimeInput(),
        #     'closing_time': forms.TimeInput(),
        #     'ammenities': forms.SelectMultiple(attrs={'style':'height:auto;'}),
        #     'payment_methods': forms.SelectMultiple(attrs={'style':'height:auto;'}),
        #     'mobile_no': forms.TextInput(attrs={'pattern':'[0-9]{10}'}),
        #     'pincode': forms.TextInput(attrs={'pattern': '[0-9]{6}'}),
        # }
