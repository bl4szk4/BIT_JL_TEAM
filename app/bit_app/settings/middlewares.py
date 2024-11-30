import jwt
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from bit_app import settings


class DeprecatedJWTTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        if "access_token" in request.COOKIES and "refresh_token" in request.COOKIES:
            try:
                token = jwt.decode(
                    request.COOKIES["access_token"], settings.SECRET_KEY, algorithms=["HS256"]
                )

                if token["iat"] < 1707090300:
                    response = self.get_response(request)
                    response.status_code = 401
                    response.data = {"detail": "Token is deprecated."}
                    response.delete_cookie("access_token")
                    response.delete_cookie("refresh_token")
                    RefreshToken(request.COOKIES["refresh_token"]).blacklist()
                    return response

                try:
                    RefreshToken(request.COOKIES["refresh_token"]).check_blacklist()
                except TokenError:
                    response = self.get_response(request)
                    response.status_code = 401
                    response.data = {"detail": "Token is blacklisted."}
                    response.delete_cookie("access_token")
                    response.delete_cookie("refresh_token")
                    return response

            except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
                pass

        response = self.get_response(request)

        return response
