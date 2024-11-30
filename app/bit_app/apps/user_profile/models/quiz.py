from django.db import models
from bit_app.apps.user_profile.models.user_profile import UserProfile

class Quiz(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='quiz')
