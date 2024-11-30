from django.db import models

from bit_app.apps.user_profile.models.quiz import Quiz


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    name = models.CharField(max_length=255)
    response = models.BooleanField(default=False)
