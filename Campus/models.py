from django.db import models


# Create your models here.

class Campus(models.Model):
    campusName = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Campus"

    def __str__(self):
        return self.campusName


class Room(models.Model):
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    floorNumber = models.CharField(max_length=2)
    roomNumber = models.CharField(max_length=5)
    roomID = models.CharField(max_length=10)

    def __str__(self):
        return self.roomID
