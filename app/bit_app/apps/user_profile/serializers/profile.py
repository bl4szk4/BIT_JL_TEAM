from rest_framework import serializers

from bit_app.apps.common.models import Location
from bit_app.apps.user_profile.models import UserProfile


class TraitSerializer(serializers.Serializer):
    key = serializers.ChoiceField(
        choices=[
            "Adventurousness",
            "Conscientiousness",
            "Extraversion",
            "Neuroticism",
            "Openness",
            "Perseverance",
            "Social Connectedness",
            "Curiosity",
            "Risk Tolerance",
            "Emotional Resonance",
        ],
        help_text="The name of the trait",
    )
    value = serializers.IntegerField(
        help_text="The value of the trait on a defined scale",
    )


class ProfileCharacterSerializer(serializers.Serializer):
    traits = serializers.ListSerializer(
        child=TraitSerializer(),
        help_text="List of traits with their integer values",
    )


class UserProfileSerializer(serializers.ModelSerializer):
    location = serializers.CharField(allow_null=True, required=False)
    character = ProfileCharacterSerializer(required=False, allow_null=True)

    class Meta:
        model = UserProfile
        fields = (
            "username",
            "age",
            "location",
            "character",
        )

    def validate_location(self, value: str) -> Location:
        if not value:
            return None
        try:
            location = Location.objects.get(city=value)
        except Location.DoesNotExist:
            raise serializers.ValidationError(f"Location '{value}' doesn't exist.")
        return location

    def validate_character(self, value):
        if not value:
            return {}
        serializer = ProfileCharacterSerializer(data=value)
        if not serializer.is_valid():
            raise serializers.ValidationError(serializer.errors)
        return serializer.validated_data

    def create(self, validated_data):
        location = validated_data.pop("location", None)
        character = validated_data.pop("character", None)
        instance = UserProfile.objects.create(**validated_data)
        if location:
            instance.location = location
        if character:
            instance.character = character
        instance.save()
        return instance

    def update(self, instance, validated_data):
        location = validated_data.pop("location", None)
        character = validated_data.pop("character", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if location:
            instance.location = location
        if character:
            instance.character = character
        instance.save()
        return instance
