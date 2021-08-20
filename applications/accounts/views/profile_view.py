from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import Profile
from applications.serializers.profile_serializer import ProfileSerializer

class ProfileAPIView(APIView):

    def get(self, request):
        profiles = Profile.objects.all()
        profiles_serializer = ProfileSerializer(profiles, many = True)
        return Response(profiles_serializer.data)