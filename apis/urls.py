from rest_framework.routers import DefaultRouter

from apis.rooms.view import RoomViewSet, RoomImageViewSet

router = DefaultRouter()

router.register(r"rooms", RoomViewSet, basename="room")
router.register(r"room-images", RoomImageViewSet, basename="room_image")

urlpatterns = router.urls
