from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from martor.models import MartorField

from blog.choices import STATUS
from .category import Category
from .tag import Tag


class Post(models.Model):
    """
    Fields: title, slug, description, text, created_date, updated_date,
    preview_image - Each field is specified as a class attribute, and each
    attribute maps to a database column.

    Relations fields: author, category - ForeignKey. A many-to-one relationship.
    tag - ManyToManyFields. A many-to-many relationship.

    Parameters: max_length - CharField (and its subclasses) require a max_length
    argument which specifies the size of the VARCHAR database field used to
    store the data;
    unique - If True, this field must be unique throughout the table.
    default - The default value for the field. This can be a value or a
    callable object. If callable it will be called every time a new object is
    created;
    blank - If True, the field is allowed to be blank;
    through - Django will automatically generate a table to manage many-to-many
    relationships. However, if you want to manually specify the intermediary
    table;
    upload_to - This attribute provides a way of setting the upload directory
    and file name;
    null - If True, Django will store empty values as NULL in the database.
    """
    author = models.ForeignKey(User, default='', on_delete=models.SET_DEFAULT)
    category = models.ForeignKey(Category, default='',
                                 on_delete=models.SET_DEFAULT)
    tag = models.ManyToManyField(Tag, blank=False, through='TagToPost')
    status = models.IntegerField(choices=STATUS, default=STATUS.draft)
    title = models.CharField(max_length=200, unique=True, blank=False)
    slug = models.SlugField(max_length=100, unique=True, default='')
    description = MartorField(default='', blank=False)
    text = MartorField(default='', blank=False)
    created_date = models.DateTimeField(auto_now_add=True, blank=True,
                                        null=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    preview_image = models.ImageField(upload_to="image/", blank=True,
                                      null=True)

    def get_absolute_url(self):
        """
        Method to tell Django how to calculate the canonical URL for an object.
        :return: a string that can be used to refer to the object over HTTP.
        """
        return reverse('post', args=(self.slug, ))

    def tags(self):
        """
        Additional function for changing all tag objects in one string tag
        (used in admin.py)
        :return: human-readable represent all tags
        """
        return ', '.join(tg.title for tg in self.tag.all())

    def save(self, *args, **kwargs):
        """
        Using for customized saving behavior.
        """
        self.slug = self.slug.lower()
        super().save(*args, **kwargs)

    class Meta:
        """
        Attributes:
        verbose_name - A human-readable name for the object, singular;
        verbose_name_plural - The plural name for the object;
        ordering - This is a tuple or list of strings and/or query expressions.
        Each string is a field name with an optional “-” prefix, which
        indicates descending order. Fields without a leading “-” will be ordered
        ascending. Use the string “?” to order randomly.
        """
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-id']


class TagToPost(models.Model):
    """
    Class for many-to-many relationship.
    Fields: post, tag - ForeignKey. A many-to-one relationship.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        """
        Method is called whenever you call str() on an object. Django uses
        str(obj) in a number of places. Most notably, to display an object in
        the Django admin site and as the value inserted into a template when it
        displays an object.
        :return: human-readable representation of the model
        """
        return ''

    class Meta:
        """
        Attributes:
        verbose_name - A human-readable name for the object, singular;
        verbose_name_plural - The plural name for the object;
        """
        verbose_name = "Tag to post"
        verbose_name_plural = "Tags to post"
