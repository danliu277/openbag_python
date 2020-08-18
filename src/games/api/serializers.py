from rest_framework import serializers

from games.models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'genre', 'sales_price', 'vendor_cost', 'stock', 'threshold')