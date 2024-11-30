from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from bit_app.apps.user.serializers import UserRegisterSerializer
from bit_app.apps.user.services import UserCreateService


class RegisterAccountView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer

    @transaction.atomic
    @swagger_auto_schema(
        response={status.HTTP_201_CREATED: "message"}, serializer_class=UserRegisterSerializer()
    )
    def post(self, request) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        user = UserCreateService(
            email=validated_data["email"],
        ).create_new_user(password=validated_data["password"])

        return Response(
            status=status.HTTP_201_CREATED,
            data={"message": f"{user.username} registered successfully!"},
        )
