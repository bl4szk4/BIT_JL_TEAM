# Register your models here.
from django.contrib import admin

from bit_app.apps.hobby.models import Hobby, HobbyEmbedding


@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("id", "name")


@admin.register(HobbyEmbedding)
class HobbyEmbeddingAdmin(admin.ModelAdmin):
    list_display = ("id", "hobby")
    list_search_fields = ("hobby",)
    autocomplete_fields = ("hobby",)
