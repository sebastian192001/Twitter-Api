from rest_framework import viewsets
from core.models import SocialPost
from applications.serializers.socialpost_serializer import SocialPostSerializer  

class SocialPostViewSet(viewsets.ModelViewSet):
    serializer_class = SocialPostSerializer
    queryset = SocialPost.objects.all()

