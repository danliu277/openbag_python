from vendors.models import Vendor
from .serializers import VendorSerializer

from rest_framework import viewsets

class VendorViewSet(viewsets.ModelViewSet):
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()