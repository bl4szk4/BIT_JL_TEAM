from rest_framework import serializers

from bit_app.apps.user_profile.models import UserProfile
from bit_app.apps.common.models import Location


class UserProfileSerializer(serializers.ModelSerializer):
    location = serializers.CharField(allow_null=True, required=False)

    class Meta:
        model = UserProfile
        fields = (
            "username",
            "age",
            "location",
        )


    def validate_location(self, value: str) -> Location:
        if not value:
            return None
        try:
            location = Location.objects.get(city=value)
        except Location.DoesNotExist:
            raise serializers.ValidationError(f"Location '{value}' doesn't exist.")
        return location

    def create(self, validated_data):
        location = validated_data.pop("location", None)
        instance = UserProfile.objects.create(**validated_data)
        instance.location = location
        instance.save()
        return instance

    def update(self, instance, validated_data):
        location = validated_data.pop("location", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if location:
            instance.location = location
        instance.save()
        return instance
