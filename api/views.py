from rest_framework import generics
from adventure.models import Room, Player
from .serializers import RoomSerializer, PlayerSerializer

class ListRoom(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class DetailRoom(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class ListPlayer(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class DetailPlayer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
