from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins

from bit_app.apps.hobby.models import Hobby
from bit_app.apps.hobby.serializers import HobbySerializer
from bit_app.apps.user_profile.models import UserProfile


class HobbyMatchingViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = Hobby.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = HobbySerializer

    def list(self, request: Request) -> Response:
        profile = UserProfile.objects.select_related('embeddings').get(user=self.request.user)
