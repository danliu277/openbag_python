from sales.models import Sales
from .serializers import SalesSerializer

from rest_framework import viewsets

class SalesViewSet(viewsets.ModelViewSet):
    serializer_class = SalesSerializer
    queryset = Sales.objects.all()