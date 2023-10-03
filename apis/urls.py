from rest_framework.routers import DefaultRouter

from apis.rooms.view import RoomViewSet

router = DefaultRouter()

router.register(r'rooms', RoomViewSet, basename='room')

urlpatterns = router.urls
