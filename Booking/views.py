import datetime

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication



from .models import Booking
from .serializer import BookingSerializer


# Create your views here.
class AllBooking(APIView):
    serializer_class = BookingSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('roomID', 'emailID', 'bookingID')
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):

        booking = Booking.objects.all()

        serializer = BookingSerializer(booking, many=True)
        return Response(serializer.data)

    def get_queryset(self):              #Gets all bookings/rooms during timeframe specified by booking?startDate=YYYY-MM-DD HH:MM&endDate=YYYY-MM-DD HH:MM
        try:

            start = self.request.query_params.getlist('startDate')
            end = self.request.query_params.getlist('endDate')

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
    def post(self, request, format=None):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            room = serializer.validated_data['roomID']
            start = serializer.validated_data['startDate']
            end = serializer.validated_data['endDate']
            email = serializer.validated_data['emailID']

            if room != '':
                sameRoomTimeFrame = Booking.objects.filter(roomID=room, endDate__gt=start, startDate__lt=end)  #Prevent booking for same room at same time
                sameUserTimeFrame = Booking.objects.filter(endDate__gt=start, startDate__lt=end, emailID=email) #Prevent user from booking the same time period on same day  in different rooms

                if not sameUserTimeFrame and not sameRoomTimeFrame:
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                elif serializer.is_valid() and sameRoomTimeFrame:
                    # bookingDuplicate = bookingCheck[0]
                    # serializer = BookingSerializer(bookingDuplicate)
                    # return Response(serializer.data)
                    return Response("error, this room is already booked for this time")
                elif serializer.is_valid() and sameUserTimeFrame:
                    return Response("Error, you cannot make another booking during a time period in which you already have one.")
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class BookingView(APIView):
    serializer_class = BookingSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('roomID', 'emailID', 'bookingID')


    def get(self, request, *args, **kwargs):
        email = self.request.query_params.get('emailID')
        id = self.request.query_params.get('bookingID')
        booking = Booking.objects.get(bookingID=id, emailID=email)

        serializer = BookingSerializer(booking)
        return Response(serializer.data)

    def delete(self, request, format=None):
        id = self.request.query_params.get('bookingID')
        booking = Booking.objects.filter(bookingID=id)
        booking.delete()
        return Response(status=status.HTTP_200_OK)

class UserBookingPageView(APIView):
    serializer_class = BookingSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('emailID')


    def get(self, request, *args, **kwargs):
        email = self.request.query_params.get('emailID')
        booking = Booking.objects.filter(emailID=email)

        serializer = BookingSerializer(booking, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def getBookings(request):
    if request.method == 'GET':
        booking = Booking.objects.all()
        serializer = BookingSerializer(booking, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = {
            'roomID': request.data.get('roomID'),
            'startDate': request.data.get('startDate'),
            'endDate': request.data.get('endDate'),
            'emailID': request.data.get('emailID')
        }
        serializer = BookingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)