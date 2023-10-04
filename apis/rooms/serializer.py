from rest_framework.serializers import ModelSerializer, SerializerMethodField

from rooms.models import Room, RoomImage, Amenity


class RoomImageSerializer(ModelSerializer):
    class Meta:
        model = RoomImage
        fields = "__all__"


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = "__all__"


class RoomSerializer(ModelSerializer):
    first_image = SerializerMethodField()
    amenities = AmenitySerializer(
        many=True,
    )

    def get_first_image(self, room):
        first_image = room.images.first()

        if first_image:
            request = self.context.get("request")
            image_url = request.build_absolute_uri(first_image.image.url)
            return image_url

        return None

    class Meta:
        model = Room
        exclude = ["title", "host"]


class RoomDetailSerializer(ModelSerializer):
    images = RoomImageSerializer(many=True, read_only=True)
    amenities = AmenitySerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = "__all__"
