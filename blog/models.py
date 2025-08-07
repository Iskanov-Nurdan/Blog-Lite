from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории" 

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    views_count = models.PositiveIntegerField(default=0)



    def str(self):
        return self.title
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты" 


class SubPost(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='subposts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def str(self):
        return self.title
    
    class Meta:
        verbose_name = "Подпост"
        verbose_name_plural = "Подпосты" 


