VALID_BLOG_REVERSE = (
    ('/', 'posts', {}),
    ('/feeds/atom.xml', 'rss_feed', {}),
    ('/categories/', 'categories', {}),
    ('/test/', 'post', {'slug': 'test'})
)

ERROR_BLOG_REVERSE = (
    ('/hello/', 'hello', {}),
    ('/abc123/', 'random', {'random': 'random'}),
    ('/', 'post', {}),
    ('/random/', 'post', {'test': 'random'})
)

INVALID_BLOG_REVERSE = (
    ('feeds/atom.xml', 'rss_feed', {}),
    ('/', 'post', {'slug': 'test'})
)
