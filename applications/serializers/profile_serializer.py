from rest_framework import serializers
from core.models import Profile

class ProfileSerializer(serializers.ModelSerializer):

    followers = serializers.StringRelatedField(many=True)

    class Meta:
        model = Profile
        fields = '__all__'