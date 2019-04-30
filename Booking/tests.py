from django.test import TestCase, Client

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.utils import json

from Booking.models import Booking

client = Client()

class BookingTest(TestCase):

    def setUp(self):
        self.valid_payload = {
            "startDate": "2011-09-27T18:30:49-0300",
            "endDate": "2012-09-27T18:30:49-0300",
            "roomID": "B310",
            "emailID": "12"
        }
        self.invalid_payload = {
            'roomID': 'B310',
            'startDate': '2014-09-27T18:30:49-0300',
            'endDate': '2014-09-27T18:30:49-0300',
            'emailID': '12'
        }

    def testValidBooking(self):
        response = client.post(
            reverse('getBookings'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def testInvalidBooking(self):
        response = client.post(
            reverse('getBookings'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)