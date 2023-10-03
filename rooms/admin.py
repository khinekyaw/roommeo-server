from django.contrib import admin

from rooms.models import Room, RoomImage, Amenity

admin.site.register(Room)
admin.site.register(RoomImage)
admin.site.register(Amenity)
