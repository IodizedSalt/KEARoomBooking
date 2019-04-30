from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from Registration.serializer import UserSerializer
from .models import User

# Create your tests here.
class UserTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        User.objects.create(first_name="Billy", last_name="Bobby", username="BilBob", email="Billy@Bobby.com")
        User.objects.create(first_name="Bobby", last_name="Billy", username="BobBil", email="Bobby@Bobby.com")


    def testUserName(self):
        userBilly = User.objects.get(first_name="Billy")
        userBobby = User.objects.get(first_name="Bobby")
        self.assertTrue(
            userBilly.getUser(), "Billy has username BilBob")
        self.assertTrue(
            userBobby.getUser(), "Bobby has username BobBil")
