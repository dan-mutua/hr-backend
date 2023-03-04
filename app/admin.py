from django.contrib import admin

# Register your models here.
from .models import Employee, Asset

admin.site.register(Employee)
admin.site.register(Asset)