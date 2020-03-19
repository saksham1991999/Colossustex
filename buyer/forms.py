from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from . import models
from supplier.models import supplier
from agent.models import agent
from core import models as coremodels
from hr import models as hrmodels


class SampleRequestForm(forms.ModelForm):
    class Meta:
        model = models.sample_request
        fields = '__all__'