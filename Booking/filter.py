import django_filters
from .models import Booking

class DateFilter(django_filters.FilterSet):
    class Meta:
        model = Booking
        fields = ['startDate', ]
