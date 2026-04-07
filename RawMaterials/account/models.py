from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Customuser(AbstractUser):
    ROLE_CHOICES=[
        ('admin','admin'),
        ('customer','customer'),
        ('contractor','contractor'),
    ]
    role=models.CharField(max_length=100,choices=ROLE_CHOICES)
    