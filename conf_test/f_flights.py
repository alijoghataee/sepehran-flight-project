from datetime import datetime, timedelta
from typing import List

import pytest

from flights.models import Flight, FlightStatus


@pytest.fixture
def f_flight():
    def create_flight(
            count: int = 3,
            params: dict[str, str | int | datetime | FlightStatus | List[str | int | datetime | FlightStatus]] = None
    ) -> List[Flight]:
        params = params or {}

        sample_data = {
            "flight_number": "SP100",
            "origin": "THR",
            "destination": "TBZ",
            "departure_time": datetime.now(),
            "arrival_time": datetime.now() + timedelta(hours=1),
            "aircraft_type": "A100",
            "seats_total": 100,
            "seats_available": 10,
            "status": FlightStatus.SCHEDULED,
            "process_id": "P-100"
        }

        flights = list()
        flight_field_names = [f.name for f in Flight._meta.fields]

        for i in range(count):
            data = sample_data.copy()

            if "flight_number" not in params:
                data["flight_number"] = f"{sample_data['flight_number']}{i+1}"

            for key, value in params.items():
                if not key in flight_field_names:
                    continue
                if isinstance(value, (str, int, datetime, FlightStatus)):
                    data[key] = value
                elif isinstance(value, list) and len(value) == count:
                    data[key] = value[i]
                else:
                    continue

            flights.append(Flight.objects.create(**data))
        return flights

    return create_flight