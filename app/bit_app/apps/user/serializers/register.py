from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},
        validators=[validate_password],
        required=True,
    )
    password_repeated = serializers.CharField(
        write_only=True, style={"input_type": "password"}, required=True
    )
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ("email", "password", "password_repeated")

    def validate(self, attrs):
        if attrs["password"] != attrs["password_repeated"]:
            raise serializers.ValidationError({"password": "Passwords do not match."})

        return attrs
