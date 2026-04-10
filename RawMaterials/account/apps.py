from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = 'account'
    # Add this for custom user model
    label = 'account'
