import pytest

from blog.models import Post


@pytest.fixture
def post_model():
    """
    Parametrized fixture. Return Post object by default without any attributes.
    """
    def update_model(**kwargs):
        return Post(**kwargs)
    return update_model
