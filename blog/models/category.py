from django.db import models
from django.urls import reverse


class Category(models.Model):
    """
    Fields: title, slug - Each field is specified as a class attribute, and
    each attribute maps to a database column.

    Parameters: max_length - CharField (and its subclasses) require a max_length
    argument which specifies the size of the VARCHAR database field used to
    store the data;
    unique - If True, this field must be unique throughout the table.
    default - The default value for the field. This can be a value or a
    callable object. If callable it will be called every time a new object is
    created.
    """
    title = models.CharField(max_length=200, unique=True, default='')
    slug = models.SlugField(max_length=200, unique=True, default='')

    def get_absolute_url(self):
        """
        Method to tell Django how to calculate the canonical URL for an object.
        :return: a string that can be used to refer to the object over HTTP.
        """
        return reverse('category', args=(self.slug, ))

    def __str__(self):
        """
        Method is called whenever you call str() on an object. Django uses
        str(obj) in a number of places. Most notably, to display an object in
        the Django admin site and as the value inserted into a template when it
        displays an object.
        :return: human-readable representation of the model
        """
        return self.title

    class Meta:
        """
        Attributes:
        verbose_name - A human-readable name for the object, singular;
        verbose_name_plural - The plural name for the object.
        """
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
