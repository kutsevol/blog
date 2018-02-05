VALID_VIEW_RESOLVE = (
    ('PostListView', 'posts', {}),
    ('PostView', 'post', {'slug': 'test'})
)

ERROR_VIEW_RESOLVE = (
    ('TestView', 'test', {}),
    ('PostView', 'post_view', {}),
    ('PostsFeed', 'rss_feed', {'slug': 'random'}),
    ('PostView', 'post', {'test': 'random'}),
)

INVALID_VIEW_RESOLVE = (
    ('PostsListView', 'posts', {}),
    ('PostsView', 'post', {'slug': 'test'})
)
