from django.urls import reverse_lazy

from blog.models import Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class BlogListView(ListView):
    model = Blog

class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "post", "image",)
    success_url = reverse_lazy('blog:blog_list'),

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "post", "image")
    success_url = reverse_lazy('blog:blog_list')

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')

class BlogDetailView(DetailView):
    model = Blog

