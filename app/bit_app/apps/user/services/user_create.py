from django.contrib.auth import get_user_model
from rest_framework.serializers import ValidationError

User = get_user_model()


class UserCreateService:
    def __init__(self, email: str) -> None:
        self.email = email.lower().strip()

    def create_new_user(self, password: str) -> User:
        if User.objects.filter(email=self.email).exists():
            raise ValidationError("Email already registered.")

        return User.objects.create_user(
            email=self.email,
            password=password,
        )
