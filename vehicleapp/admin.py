from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # Ensure this matches your custom user model

# Register the custom user model with the admin
admin.site.register(CustomUser, UserAdmin)