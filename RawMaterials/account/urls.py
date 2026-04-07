from django.urls import path
from account.views import *

urlpatterns=[
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('customer-home/',customer_home, name='customer_home'),
    path('contractor-dashboard/', contractor_dashboard, name='contractor_dashboard'),
]