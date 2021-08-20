from rest_framework import fields, serializers
from core.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user

class UserListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
    
    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'password': instance['password'],
            'email': instance['email'],
            'last_login': instance['last_login'],
            'is_superuser': instance['is_superuser'],
            'is_active': instance['is_active'],
            'date_joined': instance['date_joined'],
            'stripe_customer_id': instance['stripe_customer_id'],
        }