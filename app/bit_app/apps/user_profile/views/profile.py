from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from bit_app.apps.user_profile.models import UserProfile
from bit_app.apps.user_profile.serializers import (
    HobbyUpdateSerializer,
    ProfileCharacterSerializer,
    QuizSerializer,
    UserProfileSerializer,
)
from bit_app.apps.user_profile.services import QuizService, UserSummaryService


class ProfileViewSet(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == "upload_quiz":
            return QuizSerializer
        return UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

    def get_object(self):
        profile = self.get_queryset().first()
        return profile

    @action(methods=["GET"], detail=False)
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

    @swagger_auto_schema(
        request_body=QuizSerializer,
        responses={status.HTTP_200_OK: ""},
    )
    @action(methods=["POST"], detail=False, url_path="upload-quiz")
    def upload_quiz(self, request: Request) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        quiz = serializer.validated_data

        profile = self.get_object()
        QuizService(profile).create_quiz(quiz)

        service = UserSummaryService(profile)
        service.generate_person_summary()
        service.generate_embedding()
        character = service.generate_person_character()

        serializer = ProfileCharacterSerializer(character)

        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(responses={status.HTTP_200_OK: ""}, request_body=HobbyUpdateSerializer)
    @action(methods=["POST"], detail=False, url_path="update-hobbies-profiles")
    def update_hobbies_profile(self, request: Request) -> Response:
        serializer = HobbyUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        profile = self.get_object()

        approved_hobbies = serializer.validated_data["approved_hobbies"]
        if approved_hobbies:
            profile.accepted_hobbies.extend(approved_hobbies)
            profile.accepted_hobbies = list(set(profile.accepted_hobbies))

        deleted_hobbies = serializer.validated_data["deleted_hobbies"]
        if deleted_hobbies:
            profile.rejected_hobbies.extend(deleted_hobbies)
            profile.rejected_hobbies = list(set(profile.rejected_hobbies))

        profile.save(update_fields=["accepted_hobbies", "rejected_hobbies"])

        return Response(
            {
                "message": "Hobby profile updated successfully.",
                "accepted_hobbies": profile.accepted_hobbies,
                "rejected_hobbies": profile.rejected_hobbies,
            },
            status=status.HTTP_200_OK,
        )
