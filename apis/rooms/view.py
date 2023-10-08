from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import serializers

from apis.permissions import IsHost, ReadOnly
from rooms.models import Room, RoomImage
from .serializers import RoomSerializer, RoomDetailSerializer, RoomImageSerializer


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
        room = serializer.save()
        images_data = self.request.data.getlist("images")

        for image_data in images_data:
            image_serializer = RoomImageSerializer(data={"image": image_data})
            if image_serializer.is_valid():
                image_serializer.save(room=room)
            else:
                raise serializers.ValidationError(image_serializer.errors)

    def perform_update(self, serializer):
        room = serializer.save()
        images_data = self.request.data.getlist("images")

        room.images.all().delete()

        for image_data in images_data:
            image_serializer = RoomImageSerializer(data={"image": image_data})
            if image_serializer.is_valid():
                image_serializer.save(room=room)
            else:
                raise serializers.ValidationError(image_serializer.errors)
