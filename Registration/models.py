from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
# Models are schemas/layout of the database

# class User(AbstractUser):
#     email = models.CharField(max_length=30, unique=True)
#     password1 = models.CharField(max_length=20)
#     password2 = models.CharField(max_length=20)
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.email
class User(AbstractUser):
    # email = models.CharField(max_length=30, unique=True)


    def __str__(self):
        return 'User: {} {} {} {} '.format(self.email, self.first_name, self.last_name, self.username)
