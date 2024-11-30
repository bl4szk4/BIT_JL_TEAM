from django.contrib import admin

# Register your models here.
from django.contrib import admin
from bit_app.apps.hobby.models import Hobby


@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("id", "name")
