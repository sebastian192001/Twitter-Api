from django.urls import path
from applications.accounts.views.user_view import UserAPIView, DetailUserAPIView
from applications.accounts.views.profile_view import ProfileAPIView, DetailProfileAPIView

urlpatterns = [
    path('user/', UserAPIView.as_view(), name = 'user'),
    path('user/<int:pk>/', DetailUserAPIView.as_view(), name = 'user_detail'),
    path('profile/', ProfileAPIView.as_view(), name = 'profile'),
    path('profile/<int:pk>/', DetailProfileAPIView.as_view(), name = 'profile_detail'),
]
