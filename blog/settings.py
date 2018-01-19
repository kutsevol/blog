from django.conf import settings

# Local magic variable used inside blog app.
BLOG_TITLE = getattr(settings, 'BLOG_TITLE', 'KUTSEVOL Blog')
