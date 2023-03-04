from django.urls import path, include
from rest_framework import routers
from .views import AssetViewSet, EmployeeViewSet, LeaveViewSet

router = routers.DefaultRouter()
router.register(r'assets', AssetViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'leaves', LeaveViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
