from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Room, RoomDetails
from .serializer import RoomSerializer, RoomDetailsSerializer
# Create your views here.

class AllRoom(ListAPIView):

    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('roomID', 'campus')

    def post(self, request, format=None):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomView(APIView):

    def get(self, request, pk, format=None):
        try:
            room = Room.objects.get(pk=pk)
            serializer = RoomSerializer(room)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)




###################ROOM DETAILS######################################




class AllRoomDetails(ListAPIView):

    queryset = RoomDetails.objects.all()
    serializer_class = RoomDetailsSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('roomDetailsID',)
    def post(self, request, format=None):
        serializer = RoomDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomDetailsView(APIView):

    def get(self, request, pk, format=None):
        try:
            roomDetails = RoomDetails.objects.get(pk=pk)
            rdSerializer = RoomDetailsSerializer(roomDetails)
            return Response(rdSerializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
