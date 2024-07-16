from django.shortcuts import render
from . import models

def home(request):
    context = {'posts': models.Post.objects.all(), 'title': 'Home'}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
