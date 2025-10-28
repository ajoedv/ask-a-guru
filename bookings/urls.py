from django.urls import path
from .views import my_bookings, booking_create


app_name = "bookings"


urlpatterns = [
    path("", my_bookings, name="bookings-home"),
    path("new/", booking_create, name="create"), 
]
