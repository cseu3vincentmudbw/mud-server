from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls


API_TITLE = 'Legends MUD API'
API_DESCRIPTION = 'A web API for the Legends Multi-User Dungeon (MUD) game'

schema_view = get_schema_view(title=API_TITLE)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/adv/', include('adventure.urls')),
    path('api/auth/', include('rest_auth.urls')),
    path('api/auth/register', include('rest_auth.registration.urls')),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    path('schema/', schema_view),
]
