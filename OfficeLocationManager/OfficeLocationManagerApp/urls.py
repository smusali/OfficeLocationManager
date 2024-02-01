from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OfficeViewSet, EmployeeViewSet, CoordinateViewSet

router = DefaultRouter()
router.register(r'offices', OfficeViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'coordinates', CoordinateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
