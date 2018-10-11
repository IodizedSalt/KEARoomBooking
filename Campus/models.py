from django.db import models


# Create your models here.

class Campus(models.Model):
    campusName = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Campus"

    def __str__(self):
        return self.campusName
