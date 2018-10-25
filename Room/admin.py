from django.contrib import admin

# Register your models here.

from .models import Room, RoomDetails

admin.site.register(Room)
admin.site.register(RoomDetails)
