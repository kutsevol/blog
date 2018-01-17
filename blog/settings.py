from django.conf import settings

BLOG_TITLE = getattr(settings, 'BLOG_TITLE', 'KUTSEVOL Blog')
