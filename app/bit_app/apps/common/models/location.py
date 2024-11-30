from django.contrib.gis.db.models import PointField
from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    location = PointField(geography=True, null=True, blank=True)

    def __str__(self):
        return self.city
