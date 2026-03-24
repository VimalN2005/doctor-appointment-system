from django.contrib import admin
from .models import Service, Testimonial

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")
    list_filter = ("is_active",)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "is_approved")
    list_filter = ("is_approved", "created_at")
    search_fields = ("name",)
