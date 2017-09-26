from django.views.generic import DetailView, ListView
from django.utils import timezone
from .models import Post, Category


class PostListView(ListView):
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context_object_name = 'posts'


class PostView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'


class CategoryListView(ListView):
    queryset = Category.objects.all()
    template_name = 'blog/categories.html'
    context_object_name = 'categories'


class CategoryView(DetailView):
    model = Category
    template_name = 'blog/category.html'
    context_object_name = 'category'
