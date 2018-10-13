from rest_framework import serializers
from .models import Room, RoomDetails

class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'


class RoomDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoomDetails
        fields = '__all__'