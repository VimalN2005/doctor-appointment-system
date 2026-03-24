from rest_framework import viewsets, mixins
from clinic.models import Service, Testimonial
from blog.models import Post
from .models import Appointment
from .serializers import (
    ServiceSerializer,
    TestimonialSerializer,
    PostSerializer,
    AppointmentSerializer,
)

class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer


class TestimonialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Testimonial.objects.filter(is_approved=True)
    serializer_class = TestimonialSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostSerializer


class AppointmentViewSet(mixins.CreateModelMixin,
                         viewsets.GenericViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
