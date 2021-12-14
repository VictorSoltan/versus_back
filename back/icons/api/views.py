from rest_framework import viewsets

from .serializers import bot_serializer, shroom_serializer
from ..models import bot, shroom


class bots_view(viewsets.ModelViewSet):
    queryset = bot.objects.all()
    serializer_class = bot_serializer

class shrooms_view(viewsets.ModelViewSet):
    queryset = shroom.objects.all()
    serializer_class = shroom_serializer