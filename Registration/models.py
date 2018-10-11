from django.db import models


# Create your models here.
# Models are schemas/layout of the database

class User(models.Model):
    emailField = models.CharField(max_length=30)
    passwordField = models.CharField(max_length=20)
    firstNameField = models.CharField(max_length=20)
    lastNameField = models.CharField(max_length=20)

    def __str__(self):
        return self.emailField
