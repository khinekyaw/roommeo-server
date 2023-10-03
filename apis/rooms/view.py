from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rooms.models import Room
from .serializer import RoomSerializer
from apis.permissions import IsHost, ReadOnly

class RoomViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsHost|ReadOnly]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
