from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from bit_app.apps.user_profile.models import UserProfile
from bit_app.apps.user_profile.serializers import UserProfileSerializer

class ProfileViewSet(viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        print(self.request.user)
        return UserProfile.objects.filter(user=self.request.user)

    def get_object(self):
        profile = self.get_queryset().first()
        print(profile)
        return profile

    @action(methods=['GET'], detail=False)
    def me(self, request: Request) -> Response:
        profile = self.get_object()
        serializer = self.get_serializer(profile)

        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @me.mapping.patch
    def update_me(self, request: Request) -> Response:
        profile = self.get_object()
        serializer = self.get_serializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_200_OK, data=serializer.data)
