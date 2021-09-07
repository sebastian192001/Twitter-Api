from rest_framework import viewsets
from core.models import SocialComment
from applications.serializers.socialcomment_serializer import SocialCommentSerializer  

class SocialCommentViewSet(viewsets.ModelViewSet):
    serializer_class = SocialCommentSerializer
    queryset = SocialComment.objects.all()

