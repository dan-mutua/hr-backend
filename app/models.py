from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    num_employees = models.IntegerField()
    email_verified = models.BooleanField(default=False)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    id_number = models.CharField(max_length=20)
    kra_pin = models.CharField(max_length=20)
    position = models.CharField(max_length=100)
    assets = models.ManyToManyField('Asset', through='AssetAssignment')

class Asset(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

class AssetAssignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    date_assigned = models.DateField(auto_now_add=True)
    date_returned = models.DateField(null=True, blank=True)
    
class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.CharField(max_length=255)
    approved = models.BooleanField(default=False)