from rest_framework import serializers

from flights.models import Flight


class FlightSerializer(serializers.ModelSerializer):
    duration_minutes = serializers.ReadOnlyField()

    class Meta:
        model = Flight
        fields = '__all__'
