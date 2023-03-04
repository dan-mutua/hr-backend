from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Asset, Employee, Leave
from .serializers import AssetSerializer, EmployeeSerializer, LeaveSerializer

# initialize the APIClient app
client = APIClient()

class AssetTestCase(APITestCase):
    def setUp(self):
        self.asset = Asset.objects.create(
            name='company laptop',
            serial_number='123456',
            description='Dell XPS 13',
            assigned_to=None,
        )
        self.valid_payload = {
            'name': 'company laptop',
            'serial_number': '123456',
            'description': 'Dell XPS 13',
            'assigned_to': None,
        }
        self.invalid_payload = {
            'name': '',
            'serial_number': '',
            'description': '',
            'assigned_to': None,
        }

    def test_get_all_assets(self):
        response = client.get(reverse('asset-list'))
        assets = Asset.objects.all()
        serializer = AssetSerializer(assets, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_asset(self):
        response = client.post(reverse('asset-list'), data=self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_asset(self):
        response = client.post(reverse('asset-list'), data=self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class EmployeeTestCase(APITestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            name='John Doe',
            email='johndoe@example.com',
            password='password',
            date_of_birth='1990-01-01',
            phone_number='1234567890',
            id_number='1234567890',
            kra_pin='1234567890',
            position='Front End Developer',
        )
        self.valid_payload = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'password': 'password',
            'date_of_birth': '1990-01-01',
            'phone_number': '1234567890',
            'id_number': '1234567890',
            'kra_pin': '1234567890',
            'position': 'Front End Developer',
        }
        self.invalid_payload = {
            'name': '',
            'email': 'johndoe@example.com',
            'password': '',
            'date_of_birth': '1990-01-01',
            'phone_number': '1234567890',
            'id_number': '',
            'kra_pin': '1234567890',
            'position': '',
        }

    def test_get_all_employees(self):
        response = client.get(reverse('employee-list'))
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_employee(self):
        response = client.post(reverse('employee-list'), data=self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_employee(self):
        response = client.post(reverse('employee-list'), data=self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
