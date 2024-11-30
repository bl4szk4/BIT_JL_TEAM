from django.urls import path
from rest_framework.routers import DefaultRouter

from bit_app.apps.hobby.views import HobbyMatchingViewSet

router = DefaultRouter()


router.register("hobby-matching", HobbyMatchingViewSet, basename="hobby-matching")
urlpatterns = [] + router.urls
