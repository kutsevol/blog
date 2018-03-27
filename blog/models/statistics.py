from django.db import models
from django.utils import timezone

from .post import Post


class PostStatistic(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.post.title
