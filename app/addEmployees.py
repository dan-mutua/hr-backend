from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.urls import reverse
from .forms import AddEmployeeForm

@login_required
def add_employee(request):
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            # Check if user with the given email already exists
            if User.objects.filter(email=email).exists():
                return render(request, 'add_employee.html', {'form': form, 'error': 'User with this email already exists'})
            # Create a new user account with a random password
            password = User.objects.make_random_password()
            user = User.objects.create_user(username=email, email=email, password=password)
            user.is_active = False
            user.save()
            # Send an email to the employee with their password and activation link
            subject = 'Welcome to Our Company'
            message = f'Hi,\n\nYour account has been created. Use the following credentials to login:\nEmail: {email}\nPassword: {password}\n\nClick on the following link to activate your account:\n{reverse("activate_employee", args=[user.pk])}\n\nThanks,\nCompany Admin'
            send_mail(
                subject, message, 'from@example.com', [email], fail_silently=False,
            )
            return redirect('company_dashboard')
    else:
        form = AddEmployeeForm()
    return render(request, 'add_employee.html', {'form': form})
