from django.db import models
from django.contrib.auth import get_user_model


class RoomManager(models.Manager):
    def create_room(self, validated_data):
        amenities_data = validated_data.pop("amenities")
        room = Room.objects.create(**validated_data)

        if amenities_data:
            print(amenities_data)
            for amenity_id in amenities_data:
                amenity = Amenity.objects.get(name=amenity_id.name)
                room.amenities.add(amenity)

        return room


class Room(models.Model):
    ROOM_TYPES = [
        ("single", "Single Room"),
        ("double", "Double Room"),
        ("twin", "Twin Room"),
        ("suite", "Suite"),
        ("apartment", "Apartment"),
    ]

    # Basic room information
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2)

    # Location
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)

    # Room details
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    number_of_guests = models.PositiveIntegerField()
    number_of_bedrooms = models.PositiveIntegerField()
    number_of_bathrooms = models.PositiveIntegerField()

    # Amenities (You can use a ManyToManyField for amenities)
    amenities = models.ManyToManyField("Amenity", blank=True)

    # Host (Owner of the room)
    host = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Manage
    objects = RoomManager()

    def __str__(self):
        return self.title


class RoomImage(models.Model):
    room = models.ForeignKey(Room, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="room_images/")

    def __str__(self):
        return f"Image for {self.room.title}"


class Amenity(models.Model):
    name = models.CharField(unique=True, max_length=100)
    # icon name to use in frontend
    icon = models.CharField(max_length=64)

    def __str__(self):
        return self.name
