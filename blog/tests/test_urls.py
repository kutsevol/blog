import pytest
from django.core.urlresolvers import reverse
from django.urls.exceptions import NoReverseMatch

from blog.tests.data import urls


@pytest.mark.parametrize('url, name, kwargs', urls.VALID_BLOG_REVERSE)
@pytest.mark.django_db
def test_url_reverse(url, name, kwargs):
    """
    Check correct returned result by reverse function.
    :param url: expected url
    :param name: actual view name
    :param kwargs: additionally parameters
    """
    assert url == reverse(name, kwargs=kwargs)


@pytest.mark.parametrize('url, name, kwargs', urls.ERROR_BLOG_REVERSE)
@pytest.mark.django_db
def test_error_url_reverse(url, name, kwargs):
    """
    Check error NoReverseMatch when call reverse function.
    :param url: expected url
    :param name: actual view name
    :param kwargs: additionally parameters
    """
    with pytest.raises(NoReverseMatch):
        assert url == reverse(name, kwargs=kwargs)


@pytest.mark.parametrize('url, name, kwargs', urls.INVALID_BLOG_REVERSE)
@pytest.mark.django_db
def test_invalid_url_reverse(url, name, kwargs):
    """
    Check incorrect returned result by reverse function.
    :param url: expected url
    :param name: actual view name
    :param kwargs: additionally parameters
    """
    assert url != reverse(name, kwargs=kwargs)
