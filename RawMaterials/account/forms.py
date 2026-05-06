from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customers


class RegisterForm(UserCreationForm):
    class Meta:
        model=Customers
        fields=['username','password1','password2','role']
        