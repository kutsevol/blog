from django.db.models import Count
from django.utils import timezone
from django.views.generic import DetailView, ListView

from .models import Post, Category
from .settings import BLOG_TITLE

p_values = Post.objects.values


class PostListView(ListView):
    filtered_objects = Post.objects.filter(published_date__lte=timezone.now())
    queryset = filtered_objects.order_by('-published_date')
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        # TODO Refactoring super
        context = super(PostListView, self).get_context_data(**kwargs)
        value = ('title', 'category__title')
        context['posts_category'] = p_values(*value)
        return context


class PostView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        # TODO Refactoring super
        context = super(PostView, self).get_context_data(**kwargs)
        value = ('title', 'category__title')
        context['posts_category'] = p_values(*value)
        return context


class CategoryListView(ListView):
    queryset = Category.objects.all()
    template_name = 'blog/categories.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        # TODO Refactoring super
        context = super(CategoryListView, self).get_context_data(**kwargs)

        values = ('category__title', )
        context['count_category'] = p_values(*values).order_by('category').\
            annotate(count=Count('category'))

        values = ('title', 'slug', 'published_date', 'category__title')
        context['post_category_date'] = p_values(*values).\
            order_by('-published_date')
        return context


class CategoryView(DetailView):
    model = Category
    template_name = 'blog/category.html'
    context_object_name = 'category'


class PostsFeed(ListView):
    queryset = Post.objects.all()
    template_name = 'rss/atom.xml'
    content_type = 'application/xml'
    updated = queryset[0].published_date
    posts = Post.objects.exclude(published_date__gte=timezone.now())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.posts
        context['updated'] = self.updated
        context['blog_title'] = BLOG_TITLE
        return context
