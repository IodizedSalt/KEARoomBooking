from django.db import models


# Create your models here.
# Models are schemas/layout of the database

class User(models.Model):
    emailField = models.CharField(max_length=30)
    nameField = models.CharField(max_length=20)
    passwordField = models.CharField(max_length=20)


class RegNum(models.Model):
    userNum = models.ForeignKey(User, on_delete=models.CASCADE)
