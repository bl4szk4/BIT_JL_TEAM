from django.utils import timezone
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

class IsOwnerPermissionClass(IsAuthenticated):
    def __init__(self, owner_field: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.owner_field = owner_field

    def has_object_permission(self, request, view, obj):
        return getattr(obj, self.owner_field) == request.user


def IsOwner(owner_field: str = "user") -> type(IsOwnerPermissionClass):
    class Inner(IsOwnerPermissionClass):
        def __init__(self):
            super().__init__(owner_field=owner_field)

    return Inner