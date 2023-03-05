from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # Authentication URLs
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.employer_signup_view, name='employer_signup'),

    # Employee URLs
    path('employees/add/', views.add_employee_view, name='add_employee'),
    path('employees/<int:pk>/', views.employee_detail_view, name='employee_detail'),
    path('employees/<int:pk>/edit/', views.employee_edit_view, name='employee_edit'),
    path('employees/<int:pk>/delete/', views.employee_delete_view, name='employee_delete'),
    path('employees/<int:pk>/leave/', views.leave_request_view, name='leave_request'),
    path('employees/<int:pk>/assets/', views.employee_assets_view, name='employee_assets'),

    # Employer URLs
    path('inventory/', views.inventory_view, name='inventory'),
    path('employees/<int:pk>/position/', views.employee_position_view, name='employee_position'),
    path('notifications/', views.notification_view, name='notifications'),
]
