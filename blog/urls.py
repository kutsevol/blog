from django.urls import path
from .views import PostListView, PostView, CategoryView, CategoryListView, \
    PostsFeed

urlpatterns = [
    # page with all categories
    path(r'categories/', CategoryListView.as_view(), name='categories'),
    # TODO need check this url, maybe need remove its
    path(r'category/<slug:slug>/', CategoryView.as_view(), name='category'),
    # feed rss page
    path(r'feeds/atom.xml', PostsFeed.as_view(), name='rss_feed'),
    # each post page
    path(r'<slug:slug>/', PostView.as_view(), name='post'),
    # index page
    path(r'', PostListView.as_view(), name='posts'),
]
