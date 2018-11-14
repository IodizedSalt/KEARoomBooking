"""KEARoomBooking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path
from django.contrib import admin
import Registration.views as regApp             # Ignore this error, it compiles
import Campus.views as campusApp
import Room.views as roomApp
import Booking.views as bookingApp

urlpatterns = [
    path(r'admin/', admin.site.urls),                       #Admin Panel

    path(r'booking', bookingApp.AllBooking.as_view()),  # Room Details list per Room per campus

    path(r'registration', regApp.AllUser.as_view()),           #UserRegistration

    path(r'campus', campusApp.AllCampus.as_view()),             #Campus list

    path(r'campus/room', roomApp.AllRoom.as_view()),          #Rooms list per Campus
    path(r'campus/room/details', roomApp.AllRoomDetails.as_view()),          #Room Details list per Room per campus

    # re_path(r'^booking/(?P<pk>\d+)', bookingApp.BookingView.as_view()),
    re_path(r'^booking/(?P<pk>\d+)', bookingApp.AllBooking.as_view()),

    re_path(r'^registration/(?P<pk>\d+)', regApp.UserView.as_view()),        #Figure out what this line does
    re_path(r'^campus/(?P<pk>\d+)', campusApp.CampusView.as_view()),

    re_path(r'^campus/room/(?P<pk>\d+)', roomApp.RoomView.as_view()),
    re_path(r'^campus/room/details/(?P<pk>\w+)', roomApp.RoomDetailsView.as_view()),

]
