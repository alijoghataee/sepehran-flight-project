from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from rest_framework import viewsets

from flights.filters import FlightFilterSet
from flights.models import Flight
from flights.serializers import FlightSerializer


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                name="ordering",
                location='query',
                description="Ordering options",
                required=False,
                enum=[
                    "departure_time", "-departure_time",
                    "arrival_time", "-arrival_time",
                ],
                type=str,
            )
        ],
    )
)
class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    search_fields = ['flight_number', 'origin', 'destination', 'process_id']
    filterset_class = FlightFilterSet
    ordering_fields = ['departure_time', 'arrival_time']
