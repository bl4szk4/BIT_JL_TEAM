from djangorestframework_camel_case.parser import CamelCaseJSONParser, CamelCaseMultiPartParser
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from rest_framework.request import Request
from rest_framework.response import Response

from bit_app.apps.common.permissions import IsOwner
from bit_app.apps.user_profile.models import UserProfile
from bit_app.apps.user_profile.serializers import UserProfileSerializer

class ProfileViewSet(viewsets.GenericViewSet):
    permission_classes = (IsOwner(),)
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

    def get_object(self):
        profile = self.get_queryset().first()
        self.check_object_permissions(self.request, profile)
        return profile
