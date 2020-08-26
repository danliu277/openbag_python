from rest_framework import serializers

from vendors.models import Vendor

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('id', 'email', 'name', 'address')