from rest_framework import serializers
from core.models import SocialPost, User

class SocialPostSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(many=False)
    likes = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        slug_field='username',
        queryset = User.objects.all()
     )

    class Meta:
        model = SocialPost
        fields = '__all__'