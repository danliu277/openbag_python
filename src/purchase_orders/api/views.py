from purchase_orders.models import PurchaseOrder
from .serializers import PurchaseOrderSerializer

from rest_framework import viewsets

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseOrderSerializer
    queryset = PurchaseOrder.objects.all()