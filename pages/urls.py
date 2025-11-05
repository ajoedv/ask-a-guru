from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path("about/", views.about, name="about"),
    path("sessions/", views.sessions_view, name="sessions"),
]
