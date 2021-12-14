from rest_framework import serializers

from ..models import bot, shroom

# _______OVERVIEW_________ 

class bot_serializer(serializers.ModelSerializer):
    class Meta:
        model = bot
        fields = '__all__'
  
class shroom_serializer(serializers.ModelSerializer):
    class Meta:
        model = shroom
        fields = '__all__'