# tests/test_post.py

import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from blog.models import Post

User = get_user_model()


@pytest.mark.django_db
def test_create_post():
    user = User.objects.create_user(username="testuser", password="pass")
    client = APIClient()
    client.force_authenticate(user=user)
    data = {"title": "Test", "body": "Content", "author": user.id}
    response = client.post("/api/posts/", data)
    assert response.status_code == 201
    assert Post.objects.count() == 1


@pytest.mark.django_db
def test_bulk_create():
    user = User.objects.create_user(username="bulkuser", password="pass")
    client = APIClient()
    client.force_authenticate(user=user)
    data = [
        {"title": "A", "body": "A content", "author": user.id},
        {"title": "B", "body": "B content", "author": user.id},
    ]
    response = client.post("/api/posts/bulk-create/", data, format="json")
    assert response.status_code == 201
    assert Post.objects.count() == 2
