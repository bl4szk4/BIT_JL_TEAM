from rest_framework import serializers


class HobbyUpdateSerializer(serializers.Serializer):
    approved_hobbies = serializers.ListField(
        child=serializers.IntegerField(), required=True, allow_empty=True
    )
    deleted_hobbies = serializers.ListField(
        child=serializers.IntegerField(), required=True, allow_empty=True
    )
