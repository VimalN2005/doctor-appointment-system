from django.views.generic import TemplateView
from .models import Service, Testimonial

class HomeView(TemplateView):
    template_name = "clinic/index.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["services"] = Service.objects.filter(is_active=True)
        ctx["testimonials"] = Testimonial.objects.filter(is_approved=True).order_by("-created_at")[:6]
        return ctx
