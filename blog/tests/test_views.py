import pytest
from django.urls import reverse, resolve
from django.urls.exceptions import NoReverseMatch

from blog.tests.data import views


@pytest.mark.parametrize('view, name, kwargs', views.VALID_VIEW_RESOLVE)
@pytest.mark.django_db
def test_view_resolve(view, name, kwargs):
    """
    Check create correct resolve function with all parameters.
    :param view: expected view
    :param name: actual view name
    :param kwargs: additionally parameters
    """
    resolver = resolve(reverse(name, kwargs=kwargs))
    assert view == resolver.func.__name__
    assert name == resolver.url_name
    assert kwargs == resolver.kwargs


@pytest.mark.parametrize('view, name, kwargs', views.ERROR_VIEW_RESOLVE)
@pytest.mark.django_db
def test_error_view_resolve(view, name, kwargs):
    """
    Check error NoReverseMatch when call resolve function.
    :param view: expected view
    :param name: actual view name
    :param kwargs: additionally parameters
    """
    with pytest.raises(NoReverseMatch):
        assert view == resolve(reverse(name, kwargs=kwargs)).func.__name__


@pytest.mark.parametrize('view, name, kwargs', views.INVALID_VIEW_RESOLVE)
@pytest.mark.django_db
def test_invalid_view_resolve(view, name, kwargs):
    """
    Check incorrect result when call resolve function.
    :param view: expected view
    :param name: actual view name
    :param kwargs: additionally parameters
    """
    assert view != resolve(reverse(name, kwargs=kwargs)).func.__name__
