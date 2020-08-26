from sales.models import Sale
from .serializers import SalesSerializer

from rest_framework import viewsets

class SalesViewSet(viewsets.ModelViewSet):
    serializer_class = SalesSerializer
    queryset = Sale.objects.all()