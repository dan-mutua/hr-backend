from django.db import models

# Create your models here.
class User(models.Model):
    id=models.AutoField
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=200)
         
    def __str__(self):
        return self.username
        



class Employee(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE) 
    name=models.CharField(max_length=255)
    date_of_birth=models.DateTimeField()
    phone_number=models.CharField(max_length=255)
    id_number=models.CharField(max_length=255) 
    kra_pin=models.CharField(max_length=255)
    position=models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Asset(models.Model):
    name = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL)




class LeaveDay (models.Model):
    STATUS = (('approved','APPROVED'),('unapproved','UNAPPROVED'),('decline','DECLINED'))
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    start = models.CharField(blank=False, max_length=15)
    end = models.CharField(blank=False, max_length=15)
    status = models.CharField(choices=STATUS,  default='Not Approved',max_length=15)
    reason = models.TextField()

    def __str__(self):
        return f'{self.employee} ({self.start_date} - {self.end_date})'

  
    
class Company(models.Model):
    name = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)    
