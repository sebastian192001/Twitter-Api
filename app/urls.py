from django.conf.urls import include
from django.contrib import admin
from django.urls import path, include, re_path
from applications.accounts.views.login_view import Login, Logout, UserToken

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API Documentation",
      default_version='v0.1',
      description="Public documentation of a twitter clone",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="jnavarreterodriguez19@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


    path('admin/', admin.site.urls),
    path('accounts/', include('applications.accounts.urls')),
    path('login/', Login.as_view(), name = 'Login'),
    path('logout/', Logout.as_view(), name = 'Logout'),
    path('refresh-token/', UserToken.as_view(), name = 'refresh_token'),
    path('post/', include('applications.posts.routers')),

]
