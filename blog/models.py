from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from martor.models import MartorField


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True, default='')
    slug = models.SlugField(max_length=200, unique=True, default='')

    def get_absolute_url(self):
        return reverse('category', args=(self.slug, ))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Tag(models.Model):
    title = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Post(models.Model):
    # Relations
    author = models.ForeignKey(User)
    category = models.ForeignKey(Category, default='')
    tag = models.ManyToManyField(Tag, blank=False, through='TagToPost')

    # Attributes
    title = models.CharField(max_length=200, unique=True, blank=False)
    slug = models.SlugField(max_length=100, unique=True, default='')
    description = MartorField(default='', blank=False)
    text = MartorField(default='', blank=False)
    created_date = models.DateTimeField(auto_now_add=True, blank=False,
                                        null=True)
    published_date = models.DateTimeField(blank=False, null=True)
    preview_image = models.ImageField(upload_to="image/", blank=True,
                                      null=True)

    # Functions
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('post', args=(self.slug, ))

    def tags(self):
        return ', '.join(tg.title for tg in self.tag.all())

    def save(self, *args, **kwargs):
        self.slug = self.slug.lower()
        super().save(*args, **kwargs)

    # Meta
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-id']


class TagToPost(models.Model):
    post = models.ForeignKey(Post)
    tag = models.ForeignKey(Tag)

    def __str__(self):
        return ''

    class Meta:
        verbose_name = "Tag to post"
        verbose_name_plural = "Tags to post"
