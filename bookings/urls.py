from django.urls import path
from .views import my_bookings

urlpatterns = [
    path("", my_bookings, name="bookings-home"),
]
