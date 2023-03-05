from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import LeaveRequest


class EmployerSignupForm(UserCreationForm):
    company = forms.CharField(max_length=100, required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    num_employees = forms.ChoiceField(choices=[(i, i) for i in range(1, 11)], required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'company', 'phone_number', 'num_employees', 'password1', 'password2']
        labels = {
            'username': 'Name',
            'phone_number': 'Phone Number',
            'num_employees': 'Number of Employees',
        }


class AddEmployeeForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email


class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['start_date', 'end_date', 'reason']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
        
                