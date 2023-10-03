from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apis.permissions import IsHost, ReadOnly
from rooms.models import Room
from .serializer import RoomSerializer, RoomDetailSerializer


class RoomViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsHost | ReadOnly]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return RoomDetailSerializer
        return RoomSerializer
