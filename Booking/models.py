from django.db import models
from django.conf import settings
from django.contrib.auth.models import User



# Create your models here.

# Create your models here.


class Booking(models.Model):
    roomID = models.ForeignKey('Room.Room', on_delete=models.CASCADE, to_field='roomID')
    startDate = models.DateTimeField(null=True, blank=True)
    endDate = models.DateTimeField(null=True, blank=True)
    emailID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bookingID = models.AutoField(primary_key=True)

    def __str__(self):
        return 'Booking: {} {} {} {} {} '.format(self.roomID, self.startDate, self.endDate, self.emailID, self.bookingID)




