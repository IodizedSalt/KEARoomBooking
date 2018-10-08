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
# from django.contrib import admin
# from django.urls import include, path
#
# urlpatterns = [
#     path('', include('LandingPage.urls')),
#     path('admin/', admin.site.urls),
# ]

from django.urls import path, re_path
from django.contrib import admin
import LandingPage.views as app             # Ignore this error, it compiles

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', app.AllUser.as_view()),
    re_path(r'(?P<pk>\d+)', app.UserView.as_view()),
]
