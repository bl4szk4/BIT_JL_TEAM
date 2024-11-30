from django.contrib.auth import get_user_model
from rest_framework.serializers import ValidationError

from bit_app.apps.user_profile.models import UserProfile

User = get_user_model()


class UserCreateService:
    def __init__(self, email: str) -> None:
        self.email = email.lower().strip()

    def create_new_user(self, password: str) -> User:
        if User.objects.filter(email=self.email).exists():
            raise ValidationError("Email already registered.")

        user = User.objects.create_user(
            email=self.email,
            password=password,
        )

        UserProfile.objects.create(user=user)

        return user
