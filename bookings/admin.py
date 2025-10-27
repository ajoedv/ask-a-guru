from django.contrib import admin
from .models import Booking
from .forms import AdminBookingForm


class BookingAdmin(admin.ModelAdmin):
    form = AdminBookingForm
    list_display = ("session_title", "user", "scheduled_at", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("session_title", "user__username")


admin.site.register(Booking, BookingAdmin)