from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'user_profiles', UserProfileViewSet, basename='user_list')
router.register(r'follows', FollowViewSet, basename='follows_list')
router.register(r'posts', PostListViewSet, basename='post_list_list')
router.register(r'post_likes', PostLikeViewSet, basename='post_likes')
router.register(r'comments', CommentViewSet, basename='comments_list')
router.register(r'comment_likes', CommentLikeViewSet, basename='comment_like_list')
router.register(r'story', StoryViewSet, basename='story_list')
router.register(r'saves', SaveViewSet, basename='saves_list')
router.register(r'save_items', SaveItemViewSet, basename='save_items_list')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

 ]
