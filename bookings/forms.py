from django import forms
from datetime import datetime, date, time
from django.utils import timezone
from .models import Booking


class AdminBookingForm(forms.ModelForm):
    TIME_SLOTS = [time(h, 0) for h in range(10, 17)]
    TIME_CHOICES = [("", "Select a time")] + [
        (t.strftime("%H:%M"), t.strftime("%H:%M"))
        for t in TIME_SLOTS
    ]

    date = forms.DateField(
        label="Date",
        required=True,
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "min": date.today().isoformat(),
                "class": "form-control",
                "placeholder": "yyyy-mm-dd",
            }
        ),
    )

    time_slot = forms.ChoiceField(
        label="Scheduled at",
        required=True,
        choices=TIME_CHOICES,
        help_text="",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    class Meta:
        model = Booking
        exclude = (
            "user",
            "status",
            "scheduled_at",
            "created_at",
            "updated_at",
        )
        widgets = {
            "session_title": forms.Select(attrs={"class": "form-select"}),
            "notes": forms.Textarea(
                attrs={"class": "form-control", "rows": 6}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Prefill date and time_slot when editing an existing booking
        if self.instance and self.instance.pk and self.instance.scheduled_at:
            local_dt = timezone.localtime(self.instance.scheduled_at)
            self.fields["date"].initial = local_dt.date()
            self.fields["time_slot"].initial = local_dt.strftime("%H:%M")

    def clean(self):
        cleaned = super().clean()

        missing = []
        if not cleaned.get("session_title"):
            missing.append("session title")
        if not cleaned.get("date"):
            missing.append("date")
        if not cleaned.get("time_slot"):
            missing.append("time slot")
        if missing:
            msg = "Please select: " + ", ".join(missing) + "."
            self.add_error(None, msg)

        if cleaned.get("time_slot") and cleaned.get("date"):
            try:
                hour, minute = map(int, cleaned["time_slot"].split(":"))
            except Exception:
                self.add_error("time_slot", "Invalid time format.")
                return cleaned

            combined = datetime(
                cleaned["date"].year,
                cleaned["date"].month,
                cleaned["date"].day,
                hour,
                minute,
            )
            tz = timezone.get_current_timezone()
            scheduled = timezone.make_aware(combined, tz)
            self.instance.scheduled_at = scheduled

        return cleaned
