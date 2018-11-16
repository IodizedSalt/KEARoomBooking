import random
import string
import uuid

from django.db import models

# Create your models here.
from django import forms
from datetime import datetime

# Create your models here.
from django.utils.http import int_to_base36


class Booking(models.Model):
    roomID = models.ForeignKey('Room.Room', on_delete=models.CASCADE, to_field='roomID')
    startDate = models.DateTimeField(null=True, blank=True)
    endDate = models.DateTimeField(null=True, blank=True)
    emailID = models.ForeignKey('Registration.User', to_field='emailField', on_delete=models.CASCADE)
    bookingID = models.CharField(primary_key=True, unique=True, editable=False, blank=True, max_length=6, default='000000')

    def __str__(self):
        return self.bookingID



