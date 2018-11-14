import base64

import django_filters
from django.utils.http import urlsafe_base64_encode
from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'



