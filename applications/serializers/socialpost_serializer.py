from rest_framework import serializers
from core.models import SocialPost

class SocialPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialPost
        fields = '__all__'