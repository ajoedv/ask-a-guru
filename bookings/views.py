from django.shortcuts import render


def my_bookings(request):
    return render(request, "bookings/my_bookings.html")