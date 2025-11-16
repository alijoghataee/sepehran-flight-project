import json
from datetime import datetime, timedelta

import pytest
from rest_framework.reverse import reverse

from flights.models import FlightStatus


@pytest.mark.django_db
def test_flight_create(f_client):
    url = reverse('flights:flights-list')
    data = {
        "flight_number": "SP100",
        "origin": "THR",
        "destination": "TBZ",
        "departure_time": datetime.now().isoformat(),
        "arrival_time": (datetime.now() + timedelta(hours=1)).isoformat(),
        "aircraft_type": "A100",
        "seats_total": 100,
        "seats_available": 10,
        "status": FlightStatus.SCHEDULED,
        "process_id": "P-100"
    }
    response = f_client.post(url, data)
    json_response = json.loads(response.content)

    assert response.status_code == 201
    assert json_response['success'] is True
    assert response.data['flight_number'] == 'SP100'


@pytest.mark.django_db
def test_flight_list(f_client, f_flight):
    flights = f_flight()

    url = reverse('flights:flights-list')

    response = f_client.get(url)
    json_response = json.loads(response.content)

    assert response.status_code == 200
    assert json_response['success'] is True
    assert response.data['count'] == len(flights)


@pytest.mark.django_db
def test_flight_detail(f_client, f_flight):
    flight = f_flight()[0]

    url = reverse('flights:flights-detail', kwargs={"pk": flight.id})

    response = f_client.get(url)
    json_response = json.loads(response.content)

    assert response.status_code == 200
    assert json_response['success'] is True
    assert response.data['flight_number'] == flight.flight_number


@pytest.mark.django_db
def test_flight_update(f_client, f_flight):
    flight = f_flight(count=1, params={
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
    })[0]

    url = reverse('flights:flights-detail', kwargs={"pk": flight.id})
    data = {
        "flight_number": "SP1001", # cuz fixture add 1 to flight_number
        "origin": "THR",
        "destination": "TBZ",
        "departure_time": datetime.now(),
        "arrival_time": datetime.now() + timedelta(hours=1),
        "aircraft_type": "A100",
        "seats_total": 100,
        "seats_available": 0,
        "status": FlightStatus.DELAYED,
        "process_id": "P-100"
    }
    response = f_client.put(url, data)
    json_response = json.loads(response.content)

    assert response.status_code == 200
    flight.refresh_from_db()
    assert json_response['success'] is True
    assert response.data['seats_available'] == 0
    assert response.data['status'] == FlightStatus.DELAYED


@pytest.mark.django_db
def test_flight_delete(f_client, f_flight):
    flight = f_flight()[0]

    url = reverse('flights:flights-detail', kwargs={"pk": flight.id})

    response = f_client.delete(url)
    print(response.content)
    json_response = json.loads(response.content)

    assert response.status_code == 204
    assert json_response['success'] is True
    assert response.data is None
    assert flight is None
