from django.urls import path
from account.views import user_login, user_logout, register, admin_dashboard, customer_home, contractor_dashboard

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('customer-home/', customer_home, name='customer_home'),
    path('contractor-dashboard/', contractor_dashboard, name='contractor_dashboard'),
]