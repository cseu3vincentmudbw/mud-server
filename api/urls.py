from django.urls import include, path
from django.conf.urls import url
from .views import RoomAPIView

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('adv/rooms/', RoomAPIView.as_view()),
]
