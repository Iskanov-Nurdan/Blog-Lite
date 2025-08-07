from rest_framework.routers import DefaultRouter
from .views import PostViewSet, SubPostViewSet,  CategoryViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'subposts', SubPostViewSet, basename='subposts')
router.register('categories', CategoryViewSet)


urlpatterns = router.urls