from rest_framework import serializers
from core.models import Profile, User

class ProfileSerializer(serializers.ModelSerializer):

    followers = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        slug_field='username',
        queryset = User.objects.all()
     )

    class Meta:
        model = Profile
        fields = '__all__'