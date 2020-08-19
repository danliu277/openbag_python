from rest_framework import serializers

from purchase_orders.models import PurchaseOrder

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ('id', 'game_id', 'employee_id', 'vendor_id', 'quantity')