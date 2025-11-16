from django.core.management.base import BaseCommand

import json

from core.settings import BASE_DIR
from flights.models import Flight


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('data/flights_sample.json', 'r') as f:
            data = json.load(f)
            flights_blue_print = list()
            for flight in data:
                flight.pop('flight_id', None)
                flight.pop('duration_minutes', None)
                flights_blue_print.append(Flight(**flight))
            Flight.objects.bulk_create(flights_blue_print)
            print("All sample data saved on DB")