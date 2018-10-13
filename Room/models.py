from django.db import models
# from ..Campus import Campus

# Create your models here.



class Room(models.Model):
    campus = models.ForeignKey('Campus.Campus', on_delete=models.CASCADE)
    floorNumber = models.CharField(max_length=2)
    roomNumber = models.CharField(max_length=5)
    roomID = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.roomID


class RoomDetails(models.Model):
    roomDetailsID = models.ForeignKey(Room, max_length=10, on_delete=models.CASCADE, to_field='roomID')
    # roomID = models.OneToOneField(to='Room', to_field='roomID', on_delete=models.CASCADE, unique=True)
    capacity = models.CharField(max_length=3)
    whiteboard = models.BooleanField(default=False)
    projector = models.BooleanField(default=False)

    def __str__(self):
        return self.roomDetailsID