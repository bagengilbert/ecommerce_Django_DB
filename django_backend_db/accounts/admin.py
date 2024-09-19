# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Use the existing UserAdmin to manage your CustomUser
admin.site.register(CustomUser, UserAdmin)
