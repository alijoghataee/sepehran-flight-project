from rest_framework.routers import DefaultRouter

from flights.views import FlightViewSet


app_name = "flights"

router = DefaultRouter()

router.register('flights', FlightViewSet, basename='flights')
urlpatterns = []

urlpatterns += router.urls
