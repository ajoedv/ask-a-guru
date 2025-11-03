from django.shortcuts import render, redirect, get_object_or_404
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

            # prevent double booking at the same datetime for the same user
            if Booking.objects.filter(
                user=request.user,
                scheduled_at=booking.scheduled_at
            ).exists():
                form.add_error(None, "You already have a booking at this date and time.")
                return render(request, "bookings/booking_form.html", {"form": form})

            booking.save()
            title = booking.session_title
            messages.success(request, f'Booking created for "{title}".')
            return redirect("bookings:bookings-home")
    else:
        # PREFILL from query string (?title=...)
        initial = {}
        q_title = request.GET.get("title")
        if q_title:
            initial["session_title"] = q_title

        form = AdminBookingForm(initial=initial)

    return render(request, "bookings/booking_form.html", {"form": form})


@login_required
def my_bookings(request):
    bookings = (
        Booking.objects.filter(user=request.user).order_by("-scheduled_at")
        if request.user.is_authenticated else []
    )
    return render(request, "bookings/my_bookings.html", {"bookings": bookings})


@login_required
def booking_update(request, pk):
    obj = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == "POST":
        form = AdminBookingForm(request.POST, instance=obj)
        if form.is_valid():
            tmp = form.save(commit=False)

            # prevent conflict with another booking for the same user/datetime
            if Booking.objects.filter(
                user=request.user,
                scheduled_at=tmp.scheduled_at
            ).exclude(pk=pk).exists():
                form.add_error(None, "You already have a booking at this date and time.")
                return render(
                    request,
                    "bookings/booking_form.html",
                    {"form": form, "is_update": True},
                )

            form.save()
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
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Booking cancelled.")
        return redirect("bookings:bookings-home")
    return render(
        request,
        "bookings/booking_confirm_delete.html",
        {"booking": obj},
    )
