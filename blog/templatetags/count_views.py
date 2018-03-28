from django import template

from blog.models import Post


register = template.Library()


@register.simple_tag
def get_all_posts_statistics(post):
    value = ('poststatistic__views', )
    return Post.objects.filter(slug=post).values_list(*value, flat=True).first()
