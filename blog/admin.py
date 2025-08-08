from django.contrib import admin
from .models import Category, Post, SubPost

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)
    ordering = ('-created_at',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'created_at', 'updated_at', 'views_count', 'likes_count')
    search_fields = ('title', 'body', 'author__username')
    list_filter = ('category', 'created_at')
    autocomplete_fields = ['author', 'category', 'likes']
    readonly_fields = ('created_at', 'updated_at', 'views_count')
    
    def likes_count(self, obj):
        return obj.likes.count()
    likes_count.short_description = "Количество лайков"


@admin.register(SubPost)
class SubPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'post', 'created_at', 'updated_at')
    search_fields = ('title', 'body', 'post__title')
    list_filter = ('created_at', 'post')
    autocomplete_fields = ['post']
    readonly_fields = ('created_at', 'updated_at')
