# Register your models here.
from django.contrib import admin

from bit_app.apps.user_profile.models import Question, Quiz, UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ("username",)
    list_display = (
        "id",
        "username",
        "age",
    )

    autocomplete_fields = ("location",)


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("id",)
    search_fields = ("id",)
    autocomplete_fields = ("profile",)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    autocomplete_fields = ("quiz",)
