from rest_framework import generics
from adventure.models import Room
from .serializers import RoomSerializer

class RoomAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
