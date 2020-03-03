from django.urls import include, path
from django.conf.urls import url
from .views import ListRoom, DetailRoom, ListPlayer, DetailPlayer

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('adv/rooms/', ListRoom.as_view()),
    path('adv/rooms/<int:pk>/', DetailRoom.as_view()),
    path('adv/players/', ListPlayer.as_view()),
    path('adv/players/<int:pk>/', DetailPlayer.as_view()),
]
