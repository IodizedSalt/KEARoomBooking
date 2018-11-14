import datetime
from datetime import date

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .filter import DateFilter
from .models import Booking
from .serializer import BookingSerializer


# Create your views here.
class AllBooking(ListAPIView):
    serializer_class = BookingSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('roomID', 'emailID')
    # filter_fields = ('roomID', 'emailID', 'startDate', 'endDate')

    def get_queryset(self):
        try:

            start = self.request.query_params.getlist('startDate')
            end = self.request.query_params.getlist('endDate')
            # print("original ", start)  #todo ['2018-11-15 10:00']
            # print(end)  #todo ['2018-11-15 11:00']

            stringStart = "".join(start)
            stringStart1 = stringStart.split(' ')
            ymd = stringStart1[0]
            hm = stringStart1[1]

            startYear, startMonth, startDay= ymd.split('-')

            startYear = int(startYear)
            startMonth = int(startMonth)
            startDay = int(startDay)

            hm1 = hm.split(':')
            startHour = hm1[0]
            startHour = int(startHour)
            startMinute = hm1[1]
            startMinute = int(startMinute
                              )
            # print("Start : ", "year" ,startYear , "month ",startMonth, "day ",startDay, "hour ",startHour, "min ",startMinute)
            # print(startYear ,startMonth,startDay,startHour,startMinute)

            # endYear,endMonth,endDay = booking.split('-')
            # endHour, endMinute = None
            stringEnd = "".join(end)
            stringEnd1 = stringEnd.split(' ')
            ymd1 = stringEnd1[0]
            hm2 = stringEnd1[1]

            endYear, endMonth, endDay = ymd1.split('-')

            endYear = int(endYear)
            endMonth = int(endMonth)
            endDay = int(endDay)

            hm3 = hm2.split(':')
            endHour = hm3[0]
            endHour = int(endHour)
            endMinute = hm3[1]
            endMinute = int(endMinute)

            # print("End : ", "year ",endYear , "month ",endMonth, "day ",endDay, "hour ",endHour, "min ",endMinute)
            # print(endYear,endMonth,endDay,endHour,endMinute)
            # print(Booking.objects.filter(startDate__gt=datetime.datetime(2018, 11, 14, 10, 0)).filter(endDate__lt=datetime.datetime(2018, 11, 14, 11, 0)))
            # return Booking.objects.filter(startDate__gt=datetime.datetime(2018, 11, 15, 10, 0)).filter(endDate__lt=datetime.datetime(2018, 11, 15, 10,40))
            yes = datetime.datetime(startYear, startMonth, startDay, startHour, startMinute)
            no = datetime.datetime(endYear, endMonth, endDay, endHour, endMinute)
            return Booking.objects.filter(endDate__range=(yes, no))  #todo FINISH TESTING THIS
            # return Booking.objects.filter(startDate__gte=datetime.datetime(startYear, startMonth, startDay, startHour, startMinute)).filter(endDate__lte=datetime.datetime(endYear, endMonth, endDay, endHour, endMinute))  #todo, fix ranging issue with dates
        except:
            return Booking.objects.all()
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
