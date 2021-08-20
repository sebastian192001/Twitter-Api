from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from core.models import User
from applications.serializers.user_serializer import UserSerializer, UserListSerializer

class UserAPIView(APIView):

    def get(self, request):
        users = User.objects.all().values(
            'id',
            'username',
            'password',
            'email',
            'last_login',
            'is_superuser',
            'is_active',
            'date_joined',
            'stripe_customer_id',
        )
        users_serializer = UserListSerializer(users, many = True)
        return Response(users_serializer.data)

    def post(self, request):
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status = status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        