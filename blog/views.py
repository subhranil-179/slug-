from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin,)
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  )

from blog.models import Blog

# Create your views here.

class HomeView(ListView):
    model = Blog
    template_name = 'blog/home.html'
    context_object_name = 'blog_list'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blog'
    slug_field = 'slug'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog/new.html'
    fields = ['title', 'body']
    # login_url = 'accounts:register'
    # fields = '__all__' # To include all fields in form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(UserPassesTestMixin, UpdateView):
    model = Blog
    template_name = 'blog/edit.html'
    fields = ['title', 'body']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog:home')
