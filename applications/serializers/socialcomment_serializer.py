from rest_framework import serializers
from core.models import SocialComment

class SocialCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialComment
        fields = '__all__'