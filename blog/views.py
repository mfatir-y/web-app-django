from django.shortcuts import render, get_object_or_404
from . import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

class PostListView(ListView):
    model = models.Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_posts'] = models.Post.objects.all().order_by('-date_posted')[:3]
        return context

class UserPostListView(ListView):
    model = models.Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return models.Post.objects.filter(author=user).order_by('-date_posted')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_posts'] = models.Post.objects.all().order_by('-date_posted')[:3]
        return context

class PostDetailView(DetailView):
    model = models.Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_posts'] = models.Post.objects.all().order_by('-date_posted')[:3]
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = models.Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_posts'] = models.Post.objects.all().order_by('-date_posted')[:3]
        return context

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

def about(request):
    context = {'latest_posts': models.Post.objects.all().order_by('-date_posted')[:3], 'title': 'About'}
    return render(request, 'blog/about.html', context)
