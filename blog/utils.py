from .models import Post
from django.views.generic.base import ContextMixin

def add_latest_posts(context):
    context['latest_posts'] = Post.objects.all().order_by('-date_posted')[:3]
    return context

class CommonPostsMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = add_latest_posts(context)
        
        if hasattr(self, 'title'):
            context['title'] = self.title
        return context