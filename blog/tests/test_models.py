from collections import ChainMap

import pytest

from django.contrib.auth.models import User
from django.urls.exceptions import NoReverseMatch

from blog.models import Category, Tag, TagToPost
from blog.tests.data import models


@pytest.mark.django_db
def test_get_absolute_url_min_attrs(post_model):
    """
    Check method get_absolute_url with minimal attributes in Post model.
    :param post_model: fixture
    """
    expected_url = '/test/'
    assert expected_url == post_model(**models.POST_MIN_ATTRS).\
        get_absolute_url()


@pytest.mark.django_db
def test_get_absolute_url_all_attrs(post_model):
    """
    Check method get_absolute_url with all attributes in Post model.
    :param post_model: fixture
    """
    external_attrs = {
        'author': User.objects.create_user(models.AUTHOR),
        'category': Category.objects.create(title=models.CATEGORY),
    }

    test_kwargs = ChainMap(external_attrs, models.POST_ALL_ATTRS)

    test_tag_1 = Tag.objects.create(title=models.TAG_TITLE_1)
    test_tag_2 = Tag.objects.create(title=models.TAG_TITLE_2)

    post = post_model(**test_kwargs)
    post.save()

    TagToPost.objects.create(post=post, tag=test_tag_1)
    TagToPost.objects.create(post=post, tag=test_tag_2)

    expected_url = '/test/'
    assert expected_url == post.get_absolute_url()


@pytest.mark.django_db
def test_empty_model(post_model):
    """
    Check Post model without any elements.
    :param post_model: fixture
    """
    with pytest.raises(NoReverseMatch):
        assert '/test_url/' == post_model().get_absolute_url()


@pytest.mark.django_db
def test_tags_function(post_model):
    """
    Test function tags in Post model.
    :param post_model: fixture
    """
    external_attrs = {
        'author': User.objects.create_user(models.AUTHOR),
        'category': Category.objects.create(title=models.CATEGORY),
    }

    test_kwargs = ChainMap(external_attrs, models.POST_MIN_ATTRS)

    test_tag_1 = Tag.objects.create(title=models.TAG_TITLE_1)
    test_tag_2 = Tag.objects.create(title=models.TAG_TITLE_2)

    expected_result = ', '.join((models.TAG_TITLE_1, models.TAG_TITLE_2))

    post = post_model(**test_kwargs)
    post.save()

    TagToPost.objects.create(post=post, tag=test_tag_1)
    TagToPost.objects.create(post=post, tag=test_tag_2)
    assert expected_result == post.tags()
