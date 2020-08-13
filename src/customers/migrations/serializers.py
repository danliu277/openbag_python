from rest_framework import serializers

from customers.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'name', 'address', 'email')