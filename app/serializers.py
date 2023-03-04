from rest_framework import serializers
from .models import Asset, Employee, LeaveDay

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'email', 'name', 'date_of_birth', 'phone_number', 'id_number', 'kra_pin', 'is_active', 'is_staff')

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ('id', 'name', 'employee')

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveDay
        fields = ('id', 'employee', 'start_date', 'end_date', 'reason')
