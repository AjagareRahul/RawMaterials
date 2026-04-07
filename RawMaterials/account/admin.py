from django.contrib import admin
from .models import Customuser
# Register your models here.

'''class showuser(admin.ModelAdmin):
    model=Customuser()
    list_display=[
        ('admin','customer','constructor'),
    ]'''
admin.site.register(Customuser)