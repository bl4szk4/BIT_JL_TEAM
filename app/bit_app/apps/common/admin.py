from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin

# Register your models here.
from bit_app.apps.common.models import Location

@admin.register(Location)
class CityAdmin(GISModelAdmin):
    search_fields = ("city",)
    list_display = ("city", "id", "country")
