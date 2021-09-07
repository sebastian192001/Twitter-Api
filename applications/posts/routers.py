from applications.posts.views.comment_view import SocialCommentViewSet
from rest_framework import routers, urlpatterns
from rest_framework.routers import DefaultRouter
from applications.posts.views.post_view import SocialPostViewSet
from applications.posts.views.comment_view import SocialCommentViewSet

router = DefaultRouter()


router.register(r'socialpost',SocialPostViewSet)
router.register(r'socialcomment',SocialCommentViewSet)

urlpatterns = router.urls
