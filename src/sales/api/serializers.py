from rest_framework import serializers

from sales.models import Sales

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ('id', 'customer_id', 'game_id', 'employee_id', 'quantity')