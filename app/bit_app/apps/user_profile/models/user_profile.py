from django.conf import settings
from django.db import models

from bit_app.apps.common.models import Location


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
        blank=True,
        null=True,
    )
    username = models.CharField(max_length=100, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=True, null=True)

    summary = models.TextField(blank=True, null=True)
    character = models.JSONField(blank=True, null=True, default=dict)

    accepted_hobbies = models.JSONField(default=list, blank=True, null=True)
    rejected_hobbies = models.JSONField(default=list, blank=True, null=True)
