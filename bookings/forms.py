from django import forms
from datetime import datetime, date, time
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Booking


class AdminBookingForm(forms.ModelForm):
    TIME_SLOTS = [time(h, 0) for h in range(10, 17)]  # 10:00 to 16:00 (last session ends 17:00)
    TIME_CHOICES = [(t.strftime("%H:%M"), t.strftime("%H:%M")) for t in TIME_SLOTS]

    date = forms.DateField(
        label="Date",
        widget=forms.DateInput(attrs={"type": "date", "min": date.today().isoformat()}),
        initial=date.today,
    )

    time_slot = forms.ChoiceField(
        label="Scheduled at",
        choices=TIME_CHOICES,
        help_text="",
    )

    class Meta:
        model = Booking
        exclude = ("scheduled_at", "created_at", "updated_at")

    def clean(self):
        cleaned_data = super().clean()
        selected_date = cleaned_data.get("date")
        selected_time = cleaned_data.get("time_slot")

        if not selected_date or not selected_time:
            raise ValidationError("Please select both a date and a time slot.")

        # Combine date and time
        hour, minute = map(int, selected_time.split(":"))
        combined = datetime(
            selected_date.year, selected_date.month, selected_date.day, hour, minute
        )
        tz = timezone.get_current_timezone()
        scheduled_at = timezone.make_aware(combined, tz)

        # Validation: prevent past date/time
        if scheduled_at < timezone.now():
            raise ValidationError("You cannot book a past date or time.")

        # Prevent duplicate session bookings
        if Booking.objects.filter(
            session_title=cleaned_data.get("session_title"),
            scheduled_at=scheduled_at
        ).exclude(pk=self.instance.pk).exists():
            raise ValidationError("This time slot is already booked for this session.")

        # Assign combined datetime to the instance
        self.instance.scheduled_at = scheduled_at
        return cleaned_data
