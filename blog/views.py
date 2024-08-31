from django.shortcuts import render, get_object_or_404
from . import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .utils import CommonPostsMixin, add_latest_posts

class PostListView(CommonPostsMixin, ListView):
    model = models.Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 8
    title = 'Home'

class UserPostListView(CommonPostsMixin, ListView):
    model = models.Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return models.Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(CommonPostsMixin, DetailView):
    model = models.Post
    title = 'Post Detail'

class PostCreateView(CommonPostsMixin, LoginRequiredMixin, CreateView):
    model = models.Post
    fields = ['title', 'content']
    title = 'Create Post'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(CommonPostsMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Post
    fields = ['title', 'content']
    title = 'Update Post'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class PostDeleteView(CommonPostsMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Post
    success_url = '/'
    title = 'Delete Post'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

def about(request):
    context = {'title': 'About'}
    context = add_latest_posts(context)
    return render(request, 'blog/about.html', context)
