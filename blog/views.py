from django.shortcuts import render
from . import models
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    context = {'posts': models.Post.objects.all(), 'title': 'Home'}
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = models.Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = models.Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = models.Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
