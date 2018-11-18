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

from django.urls import path, re_path, include
from django.contrib import admin
import Registration.views as regApp             # Ignore this error, it compiles
import Campus.views as campusApp
import Room.views as roomApp
import Booking.views as bookingApp

urlpatterns = [
    path(r'admin/', admin.site.urls),                       #Admin Panel

    path(r'booking', bookingApp.AllBooking.as_view()),  # Room Details list per Room per campus
    path('booking/cancel', bookingApp.BookingView.as_view()),        #Get bookings

    path(r'registration', include('rest_auth.registration.urls')),         #UserRegistration
    path(r'', include('rest_auth.urls')),           #UserRegistration

    path(r'campus', campusApp.AllCampus.as_view()),             #Campus list

    path(r'campus/room', roomApp.AllRoom.as_view()),          #Rooms list per Campus
    path(r'campus/room/details', roomApp.AllRoomDetails.as_view()),          #Room Details list per Room per campus

    re_path('booking/cancel/(?P<pk>\w+)', bookingApp.BookingView.as_view()),

    # re_path(r'^booking/(?P<pk>\d+)', bookingApp.BookingView.as_view()),
    re_path(r'^booking/(?P<pk>\d+)', bookingApp.AllBooking.as_view()),

    re_path(r'^registration/(?P<pk>\d+)', regApp.UserView.as_view()),
    # re_path(r'^login/(?P<pk>\d+)', regApp..as_view()),
    re_path(r'^campus/(?P<pk>\d+)', campusApp.CampusView.as_view()),

    re_path(r'^campus/room/(?P<pk>\d+)', roomApp.RoomView.as_view()),
    re_path(r'^campus/room/details/(?P<pk>\w+)', roomApp.RoomDetailsView.as_view()),

]
