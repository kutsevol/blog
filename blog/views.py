from django.db.models import Count, Q
from django.db.utils import OperationalError
from django.shortcuts import get_object_or_404, render_to_response
from django.utils import timezone
from django.views.generic import DetailView, ListView

from .choices import STATUS
from .models import Category, Post, PostStatistic, UserStatistic
from .settings import BLOG_TITLE


class PostListView(ListView):
    """
    Class based on ListView for displayed all posts on start page.

    queryset - all objects from Post models where published date >= current
    time and reverse ordering.

    template_name - path to template file for this view.

    context_object_name - name of variable to access from templates.
    """
    context_object_name = 'posts'
    queryset = Post.objects.filter(Q(status=STATUS.published)).\
        order_by('-created_date')
    template_name = 'blog/post_list.html'

    def get_context_data(self, **kwargs):
        """
        Add some extra information beyond that provided by the generic view.

        posts_category in context - get all pairs post title - category title

        :return: context in template like dict
        """
        context = super().get_context_data(**kwargs)
        value = ('title', 'category__title')
        context['posts_category'] = Post.objects.values(*value)
        return context


class PostView(DetailView):
    """
    Class based on DetailView for displayed one page.
    model - if defined then method get_queryset returned Post.objects.all() same
    behavior with queryset = Post.objects.all()
    template_name - path to template file for this view.
    context_object_name - name of variable to access from templates.
    """
    context_object_name = 'post'
    model = Post
    object = None
    template_name = 'blog/post.html'
    queryset = Post.objects.filter(Q(status=STATUS.published))

    def get_context_data(self, **kwargs):
        """
        Add some extra information beyond that provided by the generic view.
        posts_category in context - get all pairs post title - category title
        :return: context in template like dict
        """
        context = super().get_context_data(**kwargs)
        value = ('title', 'category__title')
        context['posts_category'] = Post.objects.values(*value)
        return context

    # TODO: Need to add a tests for this method.
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object, **kwargs)

        post = get_object_or_404(Post, slug=self.kwargs['slug'])

        obj_usr, crt_usr = UserStatistic.objects.get_or_create(
            post=post,
            cookie=request.META.get('HTTP_COOKIE', 'new_user'),
            defaults={'post': post, 'cookie': request.META.get('HTTP_COOKIE',
                                                               'new_user')}
        )

        obj, created = PostStatistic.objects.get_or_create(
            post=post,
            defaults={'post': post, 'date': timezone.now()}
        )

        if crt_usr:
            obj.views += 1
            obj.save(update_fields=['views'])
        context['views'] = PostStatistic.objects.get(post=post).views
        return render_to_response(
            template_name=self.template_name, context=context
        )


# TODO Need move this class and CategoryView with all functionality in
# separated app.
class CategoryListView(ListView):
    """
    Class based on DetailView for displayed one page.

    model - represents an alternative query of the form Category.objects.all()

    template_name - path to template file for this view.

    context_object_name - name of variable to access from templates.
    """
    context_object_name = 'categories'
    model = Category
    template_name = 'blog/categories.html'
    queryset = Category.objects.filter(post__status=STATUS.published).distinct()

    def get_context_data(self, **kwargs):
        """
        Add some extra information beyond that provided by the generic view.

        count_category in context - how much posts in each category, need for
        displayed numbers near category title

        post_category_date - full information for displayed data in panel
        collapse.

        :return: context in template like dict
        """
        context = super().get_context_data(**kwargs)

        values = ('category__title', )
        context['count_category'] = Post.objects.\
            filter(Q(status=STATUS.published)).values(*values).\
            order_by('category').annotate(count=Count('category'))

        values = ('title', 'slug', 'created_date', 'category__title')
        context['post_category_date'] = Post.objects. \
            filter(Q(status=STATUS.published)).values(*values). \
            order_by('-created_date')
        return context


class CategoryView(DetailView):
    """
    Class based on DetailView for displayed one page.

    model - represents an alternative query of the form Category.objects.all()

    template_name - path to template file for this view.

    context_object_name - name of variable to access from templates.
    """
    context_object_name = 'category'
    model = Category
    template_name = 'blog/category.html'


# TODO Need move this class and all functionality by feed rss in separated app.
class PostsFeed(ListView):
    """
    Class for feed rss is inherited from ListView.

    queryset - define a filtered list of objects you can be more specific about
    the objects that will be visible in the view

    template_name - path to template (XML represent)

    content_type - Content type to use for all HttpResponse objects, if a MIME
    type isn’t manually specified. Used with DEFAULT_CHARSET to construct the
    Content-Type header. Default: 'text/html'

    updated - variable for template used in XML <updated></updated>

    posts - variable for template used in XML, filtered posts which not
    published yet.
    """
    content_type = 'application/xml'
    template_name = 'rss/atom.xml'
    # When db not migrate and try to get some data from db raised OperationError
    # If db migrate but hasn't any data raised AttributeError
    try:
        queryset = Post.objects.all()
        updated = queryset.first().updated_date
    except (OperationalError, AttributeError):
        updated = None
    posts = Post.objects.filter(Q(status=STATUS.published))

    def get_context_data(self, **kwargs):
        """
        Add some extra information beyond that provided by the generic view.

        :return: context in template like dict
        """
        context = super().get_context_data(**kwargs)
        context['posts'] = self.posts
        context['updated'] = self.updated
        context['blog_title'] = BLOG_TITLE
        return context
