from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import authentication
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="BIT API",
        default_version="v1",
    ),
    public=True,
    permission_classes=(AllowAny,),
    authentication_classes=(authentication.SessionAuthentication,),
)

swagger_url_patterns = [
    path(
        "swagger/",
        (schema_view.with_ui("swagger", cache_timeout=0)),
        name="swagger",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="redoc-ui",
    ),
]
