from rest_framework import serializers
from core.models import SocialPost

class SocialPostSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(many=False)
    likes = serializers.StringRelatedField(many=True)

    class Meta:
        model = SocialPost
        fields = '__all__'