from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, SubPost
from .serializers import PostSerializer, SubPostSerializer
# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class SubPostViewSet(viewsets.ModelViewSet):
    queryset = SubPost.objects.all()
    serializer_class = SubPostSerializer
