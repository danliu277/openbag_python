from rest_framework import serializers

from sales.models import Sale

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('id', 'email', 'name', 'address')