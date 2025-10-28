from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AdminBookingForm
from .models import Booking


@login_required
def booking_create(request):
    if request.method == "POST":
        form = AdminBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            title = booking.session_title
            messages.success(request, f'Booking created for "{title}".')
            return redirect("bookings:bookings-home")
    else:
        form = AdminBookingForm()
    return render(request, "bookings/booking_form.html", {"form": form})


def my_bookings(request):
    bookings = (
        Booking.objects.filter(user=request.user).order_by("-scheduled_at")
        if request.user.is_authenticated else []
    )
    return render(request, "bookings/my_bookings.html", {"bookings": bookings})