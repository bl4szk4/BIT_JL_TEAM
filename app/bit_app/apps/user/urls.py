from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from bit_app.apps.user.views import CustomLoginView, CustomLogoutView, RegisterAccountView

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegisterAccountView.as_view(), name="register"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
]
