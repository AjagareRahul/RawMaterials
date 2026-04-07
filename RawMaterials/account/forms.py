from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customuser


class RegisterForm(UserCreationForm):
    class Meta:
        model=Customuser
        fields=['username','password1','password2','role']
        