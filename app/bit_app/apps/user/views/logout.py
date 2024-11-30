from dj_rest_auth.views import LogoutView

from bit_app import settings
from bit_app.settings import DOMAIN


class CustomLogoutView(LogoutView):
    def logout(self, request):
        cookie_name = settings.REST_AUTH.get("JWT_AUTH_REFRESH_COOKIE")
        if cookie_name and cookie_name in request.COOKIES:
            request.data["refresh"] = request.COOKIES.get(cookie_name)

        response = super().logout(request)
        response.cookies["access_token"]["domain"] = DOMAIN
        response.cookies["refresh_token"]["domain"] = DOMAIN

        return response
