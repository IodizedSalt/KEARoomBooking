from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Booking
from .serializer import BookingSerializer


# Create your views here.
class AllBooking(ListAPIView):
    serializer_class = BookingSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('roomID', 'emailID', 'endDate')

    def get_queryset(self):
        booking = self.request.query_params.getlist('startDate')


        return Booking.objects.exclude(startDate__in=booking)
        # return Booking.objects.all()

    def post(self, request, format=None):  # todo (3 logics in endpoint doc)
        serializer = BookingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookingView(APIView):
    # def get(self, request, pk, format=None):
    #
    #     booking = Booking.objects.get(startDate=pk)
    #     return Booking.objects.exclude(startDate=booking)
    #
    #     # try:
    #     #     booking = Booking.objects.get(pk=pk)
    #     #     # booking = Booking.objects.get(pk=self.kwargs['startDate'])
    #     #     # booking.filter(roomID__booking__startDate__lte="2018-11-14 11:00",
    #     #     #                 roomID__booking__endDate__gte="2018-11-14 15:00")
    #     #     # booking = Booking.objects.exclude(pk='startDate')
    #     #     serializer = BookingSerializer(booking)
    #     #     return Response(serializer.data)
    #     # except:
    #     #     # return Response(status=status.HTTP_404_NOT_FOUND)
    #     #     print(status)

    def delete(self, request, pk, format=None):
        booking = Booking.objects.get(pk=pk)
        booking.delete()
        return Response(status=status.HTTP_200_OK)
