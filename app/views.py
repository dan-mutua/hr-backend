from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @action(detail=True, methods=['post'])
    def assign_asset(self, request, pk=None):
        employee = self.get_object()
        asset_id = request.data.get('asset_id')
        employee.assets.add(asset_id)
        employee.save()
        return Response({'status': 'asset assigned'})

    @action(detail=True, methods=['post'])
    def update_position(self, request, pk=None):
        employee = self.get_object()
        position = request.data.get('position')
        employee.position = position
        employee.save()
        return Response({'status': 'position updated'})

 @csrf_exempt
def employer_signup(request):
    if request.method == 'POST':
        # validate and create employer account
        return JsonResponse({'success': True})
    else:
        # render employer signup form
        return JsonResponse({'success': False})

@csrf_exempt
def employer_verify_email(request):
    if request.method == 'POST':
        # validate and verify email
        return JsonResponse({'success': True})
    else:
        # render email verification form
        return JsonResponse({'success': False})

@csrf_exempt
def employer_dashboard(request):
    if request.method == 'GET':
        # display list of employees, assets, and leave days
        return JsonResponse({'employees': [], 'assets': [], 'leave_days': []})
    elif request.method == 'POST':
        # add new employee or asset, edit employee's position or role
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

@csrf_exempt
def add_employee(request):
    if request.method == 'POST':
        # validate and create employee account
        return JsonResponse({'success': True})
    else:
        # render add employee form
        return JsonResponse({'success': False})

@csrf_exempt
def employee_dashboard(request):
    if request.method == 'GET':
        # display employee's profile details
        return JsonResponse({'profile': {}})
    elif request.method == 'POST':
        # request time-off or leave days
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

@csrf_exempt
def edit_employee_profile(request):
    if request.method == 'POST':
        # validate and update employee's profile details
        return JsonResponse({'success': True})
    else:
        # render edit employee profile form
        return JsonResponse({'success': False})

@csrf_exempt
def assign_asset(request):
    if request.method == 'POST':
        # validate and assign asset to employee
        return JsonResponse({'success': True})
    else:
        # render assign asset form
        return JsonResponse({'success': False})

@csrf_exempt
def leave_days(request):
    if request.method == 'GET':
        # display leave days taken and remaining for each employee
        return JsonResponse({'leave_days': []})
    elif request.method == 'POST':
        # edit or update leave days for an employee
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})