from django.contrib import admin

# Register your models here.
from django.contrib import admin
from bit_app.apps.user_profile.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ("username",)
    list_display = ("id", "username", "age",)

    autocomplete_fields = ("location",)
