from sales.models import Sale
from .serializers import SaleSerializer

from rest_framework import viewsets

class SaleViewSet(viewsets.ModelViewSet):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()