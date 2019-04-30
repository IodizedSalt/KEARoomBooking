from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    def getUser(self):
        return self.first_name + ' has username ' + self.username

    def __str__(self):
        # return 'User: {} {} {} {} '.format(self.email, self.first_name, self.last_name, self.username)
        return self.email
