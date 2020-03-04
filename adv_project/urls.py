from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

API_TITLE = 'Legends MUD API'
API_DESCRIPTION = 'A web API for the Legends Multi-User Dungeon (MUD) game'

schema_view = get_schema_view(
   openapi.Info(
      title=API_TITLE,
      default_version='v1',
      description=API_DESCRIPTION,
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@mud-legends.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/adv/', include('adventure.urls')),
    path('api/auth/', include('rest_auth.urls')),
    path('api/auth/register', include('rest_auth.registration.urls')),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    # path('schema/', schema_view),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
