from django.conf.urls import include
from django.contrib import admin
from django.urls import path, include
from applications.accounts.views.login_view import Login, Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('applications.accounts.urls')),
    path('', Login.as_view(), name = 'Login'),
    path('logout/', Logout.as_view(), name = 'Logout'),
]
