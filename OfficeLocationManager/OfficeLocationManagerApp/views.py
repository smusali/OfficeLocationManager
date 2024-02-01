from rest_framework import viewsets
from .models import Office, Employee, Coordinate
from .serializers import OfficeSerializer, EmployeeSerializer, CoordinateSerializer
from .utils import get_current_weather

class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        coordinates = instance.coordinate
        weather = get_current_weather(coordinates.latitude, coordinates.longitude)
        data['current_weather'] = weather
        return Response(data)


class EmployeeViewSet(viewsets.ModelViewSet):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer


class CoordinateViewSet(viewsets.ModelViewSet):
	queryset = Coordinate.objects.all()
	serializer_class = CoordinateSerializer
