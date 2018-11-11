import base64
import datetime

import json
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Booking
from .serializer import BookingSerializer, startDateSerializer
# from .serializer import BookingSerializer


# class DateTimeEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, datetime.datetime):
#             return obj.isoformat()
#         elif isinstance(obj, datetime.date):
#             return obj.isoformat()
#         elif isinstance(obj, datetime.timedelta):
#             return (datetime.datetime.min + obj).time().isoformat()
#         else:
#             return super(DateTimeEncoder, self).default(obj)
# Create your views here.
class AllBooking(ListAPIView):

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('roomID', 'emailID', 'startDate')




    def post(self, request, format=None):           #todo (3 logics in endpoint doc)
        serializer = BookingSerializer(data=request.data)

        # cereal = startDateSerializer(data=request.data)
        # poop = cereal.to_representation(request.data)
        # encoded = base64.urlsafe_b64encode(poop.encode())
        # print(encoded)
        #
        # decoded = base64.urlsafe_b64decode(encoded)
        # print(decoded)
        #
        # val = DateTimeEncoder().encode(poop)
        # print(val)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookingView(APIView):

    def get(self, request, pk, format=None):
        try:
            booking = Booking.objects.get(pk=pk)
            serializer = BookingSerializer(booking)
            print(datetime.now)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        booking = Booking.objects.get(pk=pk)
        booking.delete()
        return Response(status=status.HTTP_200_OK)