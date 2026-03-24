from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("name", "preferred_date", "service", "status", "created_at")
    list_filter = ("status", "preferred_date", "service")
    search_fields = ("name", "phone", "email")
