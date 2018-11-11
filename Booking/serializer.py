import base64

from django.utils.http import urlsafe_base64_encode
from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     ret['startDate'] = ret['startDate'].strftime("%d/%m/%Y %H:%M")
    #     return ret
    class Meta:
        model = Booking
        fields = '__all__'
class startDateSerializer(serializers.ModelSerializer):

    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     ret['startDate'] = ret['startDate']
    #     return ret

    class Meta:
        model = Booking
        fields = 'startDate',

