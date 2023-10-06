from rest_framework import serializers

from rooms.models import Room, RoomImage, Amenity
from apis.accounts.serializers import UserSerializer


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ("id", "image")


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    first_image = serializers.SerializerMethodField()
    amenities = serializers.PrimaryKeyRelatedField(
        queryset=Amenity.objects.all(), many=True, write_only=True
    )
    host = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    def get_first_image(self, room):
        first_image = room.images.first()

        if first_image:
            request = self.context.get("request")
            image_url = request.build_absolute_uri(first_image.image.url)
            return image_url

        return None

    def create(self, validated_data):
        return Room.objects.create_room(validated_data)

    class Meta:
        model = Room
        fields = "__all__"
        extra_kwargs = {
            "title": {"write_only": True},
            "description": {"write_only": True},
        }


class RoomDetailSerializer(serializers.ModelSerializer):
    images = RoomImageSerializer(many=True, read_only=True)
    amenities = AmenitySerializer(many=True, read_only=True)
    host = UserSerializer(read_only=True)

    class Meta:
        model = Room
        fields = "__all__"
