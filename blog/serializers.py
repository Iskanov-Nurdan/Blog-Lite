from rest_framework import serializers
from .models import Post, SubPost

class SubPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubPost
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
