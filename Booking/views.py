import datetime

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Booking
from .serializer import BookingSerializer


# Create your views here.
class AllBooking(ListAPIView):
    serializer_class = BookingSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('roomID', 'emailID', 'bookingID')

    def get_queryset(self):              #Gets all bookings/rooms during timeframe specified by booking?startDate=YYYY-MM-DD HH:MM&endDate=YYYY-MM-DD HH:MM
        try:

            start = self.request.query_params.getlist('startDate')
            end = self.request.query_params.getlist('endDate')

            stringStart = "".join(start)
            stringStart1 = stringStart.split(' ')
            ymd = stringStart1[0]                           #Todo, refine all of these variables,
            hm = stringStart1[1]

            startYear, startMonth, startDay= ymd.split('-')

            startYear = int(startYear)
            startMonth = int(startMonth)
            startDay = int(startDay)

            hm1 = hm.split(':')
            startHour = hm1[0]
            startHour = int(startHour)
            startMinute = hm1[1]
            startMinute = int(startMinute)

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

            return Booking.objects.filter(endDate__gt=datetime.datetime(startYear, startMonth, startDay, startHour, startMinute)).filter(startDate__lt=datetime.datetime(endYear, endMonth, endDay, endHour, endMinute))  #todo, fix ranging issue with dates
        except:
            return Booking.objects.all()

    def post(self, request, format=None):  # todo (3 logics in endpoint doc)
        serializer = BookingSerializer(data=request.data)

        if serializer.is_valid():
            room = serializer.validated_data['roomID']
            start = serializer.validated_data['startDate']
            end = serializer.validated_data['endDate']

            if room != '':
                bookingCheck = Booking.objects.filter(roomID=room, endDate__gt=start, startDate__lt=end)
                if not bookingCheck:
                    serializer.save()
                elif serializer.is_valid():
                    bookingDuplicate = bookingCheck[0]
                    serializer = BookingSerializer(bookingDuplicate)
                    # return Response(serializer.data)
                    return Response("error, this room is already booked for this time") #todo make a proper response
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)






            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request, *args, **kwargs):
    #     username = self.kwargs.get('username')
    #     print(username)
    #
    #     # use this if username is being sent as a query parameter
    #     queryparam = self.request.query_params.get('username')
    #     print(queryparam)

class BookingView(APIView):
    serializer_class = BookingSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('roomID', 'emailID', 'bookingID')

    def get(self, request, *args, **kwargs):
        username = self.kwargs.get('username')
        print(username)

        # use this if username is being sent as a query parameter
        queryparam = self.request.query_params.get('username')
        print(queryparam)

    def delete(self, request, format=None):
        email = self.request.query_params.get('emailID')
        room = self.request.query_params.get('roomID')
        id = self.request.query_params.get('bookingID')
        booking = Booking.objects.filter(roomID=room, emailID=email, bookingID=id)
        booking.delete()
        return Response(status=status.HTTP_200_OK)

