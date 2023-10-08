from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsHost(BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, "host"):
            return obj.host == request.user
        if hasattr(obj, "room"):
            return obj.room.host == request.user
