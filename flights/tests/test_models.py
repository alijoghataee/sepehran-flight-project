from datetime import timedelta

import pytest

from flights.models import Flight


@pytest.mark.django_db
def test_flight_duration_minutes(f_flight):
    flight = f_flight(count=1)[0]

    assert flight.duration_minutes == (flight.arrival_time - flight.departure_time).total_seconds() / 60
