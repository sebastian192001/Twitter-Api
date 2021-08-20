from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView
from core.models import Profile
from applications.serializers.profile_serializer import ProfileSerializer

class ProfileAPIView(APIView):

    def get(self, request):
        profiles = Profile.objects.all()
        profiles_serializer = ProfileSerializer(profiles, many = True)
        return Response(profiles_serializer.data)

class DetailProfileAPIView(APIView):

    def get(self, request, pk = None):

        if request.method == 'GET':
            profile = Profile.objects.filter(id = pk).first()
            profile_serializer = ProfileSerializer(profile)
            return Response(profile_serializer.data, status = status.HTTP_202_ACCEPTED)

    def put(self, request, pk = None):

        if request.method == 'PUT':
            profile = Profile.objects.filter(id = pk).first()
            profile_serializer = ProfileSerializer(profile, data = request.data)
            if profile_serializer.is_valid():
                profile_serializer.save()
                return Response(profile_serializer.data, status = status.HTTP_202_ACCEPTED)
            return Response(profile_serializer.errors)

    