from django.db import models

# Create your models here.
from django import forms
from datetime import datetime

# Create your models here.


# class Booking(models.Model):
#     roomID = models.ForeignKey('Room.Room', on_delete=models.CASCADE, to_field='roomID')
#     startDate = forms.DateTimeField(input_formats=['%m/%d/%y %H:%M'], initial=datetime.now)
#     endDate = forms.DateTimeField(input_formats=['%m/%d/%y %H:%M'], initial=datetime.now)
#     email = models.ForeignKey('Registration.User', to_field='emailField', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.roomID
#

class Booking(models.Model):
    roomID = models.ForeignKey('Room.Room', on_delete=models.CASCADE, to_field='roomID')
    startDate = models.DateTimeField(null=True, blank=True, default=datetime.now)
    endDate = models.DateTimeField(null=True, blank=True, default=datetime.now)
    emailID = models.ForeignKey('Registration.User', to_field='emailField', on_delete=models.CASCADE)

    def __str__(self):
        return self.roomID
