from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from . import models
from supplier.models import supplier
from agent.models import agent
from buyer.models import buyer
from buyer import models as buyermodels
from supplier import models as suppliermodels
from agent import models as agentmodels
from core import models as coremodels
from hr import models as hrmodels
from django.forms import formset_factory, inlineformset_factory, modelformset_factory


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


#ENQUIRY MANAGEMENT FORMS
class InquiryForm(forms.ModelForm):
    class Meta:
        model = coremodels.inquiry
        fields = ['buyer', 'source', 'agent', 'remarks']


class InquiryProductForm(forms.ModelForm):
    class Meta:
        model = coremodels.inquiry_product
        exclude = ['inquiry']


InquiryProductFormset = formset_factory(InquiryProductForm, extra=1)

class NotifySuppliersForm(forms.ModelForm):
    class Meta:
        model = coremodels.notified_suppliers
        fields = ['suppliers']

class SupplierQuotationsForm(forms.ModelForm):
    class Meta:
        model = coremodels.supplier_quotations
        fields = ['supplier', 'product','price_kg']

SupplierQuotationsFormset = formset_factory(SupplierQuotationsForm, extra=1)


class ForwardedQuotationsForm(forms.ModelForm):
    class Meta:
        model = coremodels.forwarded_quotation
        fields = ['quotations']

class InquiryUpdateForm(forms.ModelForm):
    class Meta:
        model = coremodels.inquiry_update
        exclude = ['inquiry']

class ClosingInquiryForm(forms.ModelForm):
    class Meta:
        model = coremodels.inquiry
        fields = ['close_choice']



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

class VisitNoteForm(forms.ModelForm):
    class Meta:
        model = models.employee_visit
        exclude = ['employee']

class SuplusProductForm(forms.ModelForm):
    class Meta:
        model = coremodels.suplus_product
        fields = '__all__'

class UpdateNewsForm(forms.ModelForm):
    class Meta:
        model = coremodels.updates
        fields = '__all__'

class LeaveApplicationEmployeeForm(forms.ModelForm):
    class Meta:
        model = hrmodels.leaveapplication
        exclude = ['employee', 'status']

class InspectionForm(forms.ModelForm):
    class Meta:
        model = models.inspection
        fields = '__all__'

class BuyerComplaintForm(forms.ModelForm):
    class Meta:
        model = buyermodels.buyer_complaints
        fields = '__all__'

class SupplierComplaintForm(forms.ModelForm):
    class Meta:
        model = suppliermodels.supplier_complaints
        fields = '__all__'

class SubAgentComplaintForm(forms.ModelForm):
    class Meta:
        model = agentmodels.agent_complaints
        fields = '__all__'

class BuyerFeedbackForm(forms.ModelForm):
    class Meta:
        model = buyermodels.buyer_general_feedback
        fields = '__all__'

class SupplierFeedbackForm(forms.ModelForm):
    class Meta:
        model = suppliermodels.supplier_feedback
        fields = '__all__'

class SubAgentFeedbackForm(forms.ModelForm):
    class Meta:
        model = agentmodels.agent_general_feedback
        fields = '__all__'

