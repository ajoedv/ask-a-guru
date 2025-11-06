# bookings/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db import IntegrityError
from .forms import AdminBookingForm
from .models import Booking


@login_required
def booking_create(request):
    if request.method == "POST":
        form = AdminBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            if Booking.objects.filter(scheduled_at=booking.scheduled_at).exists():
                form.add_error(None, "This time slot is already booked.")
                return render(request, "bookings/booking_form.html", {"form": form})
            try:
                booking.save()
            except IntegrityError:
                form.add_error(None, "This time slot is already booked.")
                return render(request, "bookings/booking_form.html", {"form": form})
            messages.success(request, f'Booking created for "{booking.session_title}".')
            return redirect("bookings:bookings-home")
    else:
        initial = {}
        q_title = request.GET.get("title")
        if q_title:
            initial["session_title"] = q_title
        form = AdminBookingForm(initial=initial)
    return render(request, "bookings/booking_form.html", {"form": form})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by("-scheduled_at")
    return render(
        request,
        "bookings/my_bookings.html",
        {"bookings": bookings, "now": timezone.now()},
    )


@login_required
def booking_update(request, pk):
    obj = get_object_or_404(Booking, pk=pk, user=request.user)

    if obj.scheduled_at <= timezone.now():
        messages.error(request, "Past bookings cannot be edited.")
        return redirect("bookings:bookings-home")

    if request.method == "POST":
        form = AdminBookingForm(request.POST, instance=obj)
        if form.is_valid():
            tmp = form.save(commit=False)

            # block any booking at the same datetime (global), excluding current
            if Booking.objects.filter(scheduled_at=tmp.scheduled_at).exclude(pk=obj.pk).exists():
                form.add_error(None, "This time slot is already booked.")
                return render(
                    request,
                    "bookings/booking_form.html",
                    {"form": form, "is_update": True},
                )

            try:
                form.save()
            except IntegrityError:
                form.add_error(None, "This time slot is already booked.")
                return render(
                    request,
                    "bookings/booking_form.html",
                    {"form": form, "is_update": True},
                )

            messages.success(request, "Booking updated.")
            return redirect("bookings:bookings-home")
    else:
        form = AdminBookingForm(instance=obj)

    return render(
        request,
        "bookings/booking_form.html",
        {"form": form, "is_update": True},
    )


@login_required
def booking_delete(request, pk):
    obj = get_object_or_404(Booking, pk=pk, user=request.user)

    if obj.scheduled_at <= timezone.now():
        messages.error(request, "Past bookings cannot be cancelled.")
        return redirect("bookings:bookings-home")

    if request.method == "POST":
        obj.delete()
        messages.success(request, "Booking cancelled.")
        return redirect("bookings:bookings-home")

    return render(
        request,
        "bookings/booking_confirm_delete.html",
        {"booking": obj},
    )
