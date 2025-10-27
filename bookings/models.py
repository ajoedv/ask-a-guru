# bookings/models.py
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone


class Booking(models.Model):
    SESSION_CHOICES = [
        ("Design Strategy", "Design Strategy"),
        ("Photography Critique", "Photography Critique"),
        ("Brand Foundations", "Brand Foundations"),
    ]

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    session_title = models.CharField(max_length=120, choices=SESSION_CHOICES)
    scheduled_at = models.DateTimeField()
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        # Basic validation
        if self.scheduled_at < timezone.now():
            raise ValidationError("You cannot book a past date or time.")

        exists = Booking.objects.filter(
            session_title=self.session_title,
            scheduled_at=self.scheduled_at
        ).exclude(pk=self.pk).exists()
        if exists:
            raise ValidationError("This time slot is already booked for this session.")

    def __str__(self):
        return f"{self.session_title} — {self.user.username}"
