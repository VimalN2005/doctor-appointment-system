from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import (
    ServiceViewSet,
    TestimonialViewSet,
    PostViewSet,
    AppointmentViewSet,
)

router = DefaultRouter()
router.register("services", ServiceViewSet, basename="service")
router.register("testimonials", TestimonialViewSet, basename="testimonial")
router.register("posts", PostViewSet, basename="post")
router.register("appointments", AppointmentViewSet, basename="appointment")

urlpatterns = [
    path("", include(router.urls)),
]
