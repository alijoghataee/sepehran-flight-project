from django.db import models

from core.base.models import BaseModel


class FlightStatus(models.TextChoices):
    SCHEDULED = 'scheduled', 'Scheduled'
    DEPARTED = 'departed', 'Departed'
    ARRIVED = 'arrived', 'Arrived'
    CANCELLED = 'cancelled', 'Cancelled'
    DELAYED = 'delayed', 'Delayed'


class Flight(BaseModel):
    flight_number = models.CharField(max_length=50, unique=True)
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    aircraft_type = models.CharField(max_length=50)
    seats_total = models.PositiveIntegerField()
    seats_available = models.PositiveIntegerField()
    status = models.CharField(
        max_length=9,
        choices=FlightStatus.choices,
        default=FlightStatus.SCHEDULED
    )
    process_id = models.CharField(max_length=100)

    @property
    def duration_minutes(self):
        return (self.arrival_time - self.departure_time).total_seconds() / 60

    def __str__(self):
        return f"{self.flight_number} ({self.origin} → {self.destination})"
