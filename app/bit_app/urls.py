"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from bit_app.settings import ENV
from bit_app.swagger import swagger_url_patterns

urlpatterns = [
    path("auth/", include("bit_app.apps.user.urls")),
    path("", include("bit_app.apps.user_profile.urls")),
    path("", include("bit_app.apps.hobby.urls")),
    path("admin/", admin.site.urls),
]

if ENV == "development":
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
        path("admin/", admin.site.urls),
    ]
    urlpatterns += swagger_url_patterns

#
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
