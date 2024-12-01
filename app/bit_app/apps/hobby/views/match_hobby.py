from rest_framework import mixins, viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from bit_app.apps.hobby.models import Hobby
from bit_app.apps.hobby.serializers import HobbySerializer
from bit_app.apps.hobby.services import HobbyMatchingService
from bit_app.apps.user_profile.models import UserProfile


class HobbyMatchingPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 100


class HobbyMatchingViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = Hobby.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = HobbySerializer
    pagination_class = HobbyMatchingPagination

    def list(self, request: Request) -> Response:
        try:
            profile = UserProfile.objects.prefetch_related("embeddings").get(user=self.request.user)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

        hobbies_matched = HobbyMatchingService(profile).get_best_matching_hobbies()
        page = self.paginate_queryset(hobbies_matched)
        if page is not None:
            serializer = HobbySerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = HobbySerializer(hobbies_matched, many=True)
        return Response(serializer.data)
