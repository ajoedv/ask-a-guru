from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "session_title",
        "scheduled_at",
        "status",
        "created_at",
    )
    list_filter = ("status", "session_title")
    search_fields = ("user__username", "user__email", "session_title")
    ordering = ("-scheduled_at",)

    fields = ("user", "session_title", "notes", "scheduled_at", "status")
    readonly_fields = ("created_at", "updated_at")

    actions = ["mark_confirmed", "mark_cancelled"]

    @admin.action(description="Mark selected as confirmed")
    def mark_confirmed(self, request, queryset):
        queryset.update(status="confirmed")

    @admin.action(description="Mark selected as cancelled")
    def mark_cancelled(self, request, queryset):
        queryset.update(status="cancelled")
