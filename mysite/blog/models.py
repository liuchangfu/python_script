from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class BlogArticles(models.Model):
    # title属性为CharFiel()类型，并且以参数max_length的形式说明字段的最大的数量
    title = models.CharField(max_length=300)

    author = models.ForeignKey(User,related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


