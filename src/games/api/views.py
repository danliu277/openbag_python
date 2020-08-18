from games.models import Game
from .serializers import GameSerializer

from rest_framework import viewsets

class GameViewSet(viewsets.ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()