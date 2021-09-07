from django.conf.urls import include
from django.contrib import admin
from django.urls import path, include
from applications.accounts.views.login_view import Login, Logout, UserToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('applications.accounts.urls')),
    path('login/', Login.as_view(), name = 'Login'),
    path('logout/', Logout.as_view(), name = 'Logout'),
    path('refresh-token/', UserToken.as_view(), name = 'refresh_token'),
    path('post/', include('applications.posts.routers')),
]
