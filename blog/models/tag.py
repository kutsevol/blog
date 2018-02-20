from django.db import models


class Tag(models.Model):
    """
     Fields: title - Each field is specified as a class attribute, and
     each attribute maps to a database column.

     Parameters: max_length - CharField (and its subclasses) require a
     max_length argument which specifies the size of the VARCHAR database field
     used to store the data;
     blank - If True, the field is allowed to be blank.
     """
    title = models.CharField(max_length=200, blank=False)

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
        verbose_name - A human-readable name for the object,
        singular;
        verbose_name_plural - The plural name for the object.
        """
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
