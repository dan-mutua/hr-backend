from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Asset, Employee, LeaveDay
from .serializers import AssetSerializer, EmployeeSerializer, LeaveSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    permission_classes = [IsAuthenticated]

class LeaveViewSet(viewsets.ModelViewSet):
    queryset = LeaveDay.objects.all()
    serializer_class = LeaveSerializer
    permission_classes = [IsAuthenticated]
