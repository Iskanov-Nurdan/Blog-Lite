from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class SubPost(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='subposts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
