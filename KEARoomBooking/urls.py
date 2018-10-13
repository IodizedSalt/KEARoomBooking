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
import Registration.views as app             # Ignore this error, it compiles
import Campus.views as apps

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'registration', app.AllUser.as_view()),
    path(r'campus/', apps.AllCampus.as_view()),             #MAKE SURE YOU HAVE THE RIGHT CALL HERE (ALLCAMPUS VS CAMPUSVIEW)
    path(r'campus/room/', apps.AllRoom.as_view()),
    re_path(r'(?P<pk>\d+)', app.UserView.as_view()),        #Figure out what this line does
    re_path(r'(?P<pk>\d+)', apps.CampusView.as_view()),     #These lines are necessary orelse you get a typeError. try it out
    re_path(r'(?P<pk>\d+)', apps.RoomView.as_view()),
]
