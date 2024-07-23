from django.shortcuts import render
from . import models
from django.views.generic import ListView

def home(request):
    context = {'posts': models.Post.objects.all(), 'title': 'Home'}
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = models.Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
