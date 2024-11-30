from rest_framework import mixins, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from bit_app.apps.hobby.models import Hobby
from bit_app.apps.hobby.serializers import HobbySerializer
from bit_app.apps.hobby.services import HobbyMatchingService
from bit_app.apps.user_profile.models import UserProfile


class HobbyMatchingPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class HobbyMatchingViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = Hobby.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = HobbySerializer
    pagination_class = HobbyMatchingPagination

    def list(self, request: Request) -> Response:

        profile = UserProfile.objects.select_related("embedding").get(user=self.request.user)

        hobbies_matched = HobbyMatchingService(profile).get_best_matching_hobbies()
        page = self.paginate_queryset(hobbies_matched)
        if page is not None:
            serializer = HobbySerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = HobbySerializer(hobbies_matched, many=True)
        return Response(serializer.data)
