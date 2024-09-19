from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Add phone number field
    address = models.TextField(blank=True, null=True)  # Add address field
    
    # Avoid conflicts by setting custom related_name for groups and permissions
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_groups',  
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',  
        blank=True
    )
    
    def __str__(self):
        return self.username
