from django.urls import path
from .views import my_bookings


app_name = "bookings"


urlpatterns = [
    path("", my_bookings, name="bookings-home"),
]
