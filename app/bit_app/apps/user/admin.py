# Register your models here.
import uuid

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from bit_app.apps.user.models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = (
        "email",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "is_staff",
        "is_superuser",
        "is_active",
        "groups",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                    "username",
                )
            },
        ),
        (
            _("Account status"),
            {
                "fields": ("is_active",),
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "groups",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "username",
                    "role",
                    "is_staff",
                ),
            },
        ),
    )

    def get_changeform_initial_data(self, request):
        return {"username": str(uuid.uuid4())}


admin.site.register(CustomUser, CustomUserAdmin)
