import django_filters

from flights.models import Flight


class FlightFilterSet(django_filters.FilterSet):
    has_available_seats = django_filters.BooleanFilter(method='has_available_seats_filter')

    class Meta:
        model = Flight
        fields = {
            'departure_time': ['date'],
            'arrival_time': ['date'],
            'aircraft_type': ['exact'],
            'status': ['exact'],
        }

    def has_available_seats_filter(self, queryset, name, value):
        if value is True:
            return queryset.filter(available_seats__gt=0)
        elif value is False:
            return queryset.filter(available_seats=0)
        else:
            return queryset
