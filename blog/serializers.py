from rest_framework import serializers
from .models import Post, SubPost, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at']


class SubPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubPost
        fields = ['id', 'title', 'body', 'post', 'created_at', 'updated_at']

class PostSerializer(serializers.ModelSerializer):
    subposts = SubPostSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'author', 'created_at', 'updated_at', 'subposts']

    def create(self, validated_data):
        subposts_data = validated_data.pop('subposts', [])
        post = Post.objects.create(**validated_data)
        for sub_data in subposts_data:
            sub_data.pop('post', None)  # убираем ключ post, если есть
            SubPost.objects.create(post=post, **sub_data)
        return post

    def update(self, instance, validated_data):
        subposts_data = validated_data.pop('subposts', [])
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()

        existing_ids = [item['id'] for item in subposts_data if 'id' in item]
        instance.subpost_set.exclude(id__in=existing_ids).delete()

        for sub_data in subposts_data:
            sub_data.pop('post', None)
            if 'id' in sub_data:
                subpost = SubPost.objects.get(id=sub_data['id'], post=instance)
                subpost.title = sub_data.get('title', subpost.title)
                subpost.body = sub_data.get('body', subpost.body)
                subpost.save()
            else:
                SubPost.objects.create(post=instance, **sub_data)

        return instance
