from django.conf.urls import url
from .views import PostListView, PostView, CategoryView, CategoryListView, \
    PostsFeed

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='posts'),
    url(r'^categories/?$', CategoryListView.as_view(), name='categories'),
    url(r'^category/(?P<slug>[-\w\d\_]+)/$', CategoryView.as_view(),
        name='category'),
    url(r'^feeds/$', PostsFeed()),
    url(r'^(?P<slug>[-\w\d\_]+)/$', PostView.as_view(), name='post'),
]
