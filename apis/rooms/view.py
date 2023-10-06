from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser

from apis.permissions import IsHost, ReadOnly
from rooms.models import Room, RoomImage
from .serializers import RoomSerializer, RoomDetailSerializer


class RoomViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsHost | ReadOnly]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return RoomDetailSerializer
        return RoomSerializer

    def perform_create(self, serializer):
        # Save the room instance
        room = serializer.save()

        # Handle image uploads
        images_data = self.request.data.getlist("images")

        for image_data in images_data:
            RoomImage.objects.create(room=room, image=image_data)
