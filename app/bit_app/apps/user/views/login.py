from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomLoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        tokens = response.data
        refresh_token = tokens.get("refresh")
        access_token = tokens.get("access")

        if refresh_token:
            response.set_cookie(
                key=settings.REST_AUTH["JWT_AUTH_REFRESH_COOKIE"],
                value=refresh_token,
                httponly=True,
                secure=settings.DEBUG is False,
                samesite="Lax",
            )

        if access_token:
            response.set_cookie(
                key=settings.REST_AUTH["JWT_AUTH_COOKIE"],
                value=access_token,
                httponly=True,
                secure=settings.DEBUG is False,
                samesite="Lax",
            )

        return response
