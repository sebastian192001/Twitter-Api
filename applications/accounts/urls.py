from django.urls import path
from applications.accounts.views.user_view import UserAPIView
from applications.accounts.views.profile_view import ProfileAPIView

urlpatterns = [
    path('user/', UserAPIView.as_view(), name = 'user'),
    path('profile/', ProfileAPIView.as_view(), name = 'profile')
]
