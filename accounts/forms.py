from django import forms
from core.models import User


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class UserSignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
