from django.urls import path
from rest_framework.routers import DefaultRouter

from bit_app.apps.user_profile.views import ProfileViewSet

router = DefaultRouter()


router.register("profile", ProfileViewSet, basename="profile")
urlpatterns = [] + router.urls
