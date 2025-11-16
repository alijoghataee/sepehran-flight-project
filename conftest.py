from conf_test.f_flights import *


import pytest
from rest_framework.test import APIClient


@pytest.fixture
def f_client() -> APIClient:
    return APIClient()
