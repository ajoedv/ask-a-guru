from django.urls import path
from .views import my_bookings, booking_create, booking_update, booking_delete


app_name = "bookings"


urlpatterns = [
    path("", my_bookings, name="bookings-home"),
    path("new/", booking_create, name="create"),
    path("<int:pk>/edit/", booking_update, name="update"),
    path("<int:pk>/delete/", booking_delete, name="delete"),
]
