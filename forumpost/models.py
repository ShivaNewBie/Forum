from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class ForumPost(models.Model):
    title = models.CharField(max_length=200,unique=True)
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
           return reverse("forumpost:forum-post-view", kwargs={'id': self.id})
