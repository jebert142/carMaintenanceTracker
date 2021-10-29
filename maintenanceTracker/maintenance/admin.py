from django.contrib import admin
from .models import Vehicle, Log

# Registers models with Django
admin.site.register(Vehicle)
admin.site.register(Log)