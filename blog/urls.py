from django.conf.urls import url
from .views import PostListView, PostView, CategoryView, CategoryListView, \
    PostsFeed

urlpatterns = [
    # index page
    url(r'^$', PostListView.as_view(), name='posts'),
    # page with all categories
    url(r'^categories/?$', CategoryListView.as_view(), name='categories'),
    # TODO need check this url, maybe need remove its
    url(r'^category/(?P<slug>[-\w\d\_]+)/$', CategoryView.as_view(),
        name='category'),
    # feed rss page
    url(r'^feeds/atom.xml$', PostsFeed.as_view(), name='rss_feed'),
    # each post page
    url(r'^(?P<slug>[-\w\d\_]+)/$', PostView.as_view(), name='post'),
]
