from employees.models import Employee
from .serializers import EmployeeSerializer

from rest_framework import viewsets

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()