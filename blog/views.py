from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(is_published=True)
    template_name = "blog/list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"
    context_object_name = "post"
    slug_field = "slug"
    slug_url_kwarg = "slug"
