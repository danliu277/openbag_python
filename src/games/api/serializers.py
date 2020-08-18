from rest_framework import serializers

from employees.models import Employee

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name', 'genre', 'sales_price', 'vendor_cost', 'stock', 'threshold')