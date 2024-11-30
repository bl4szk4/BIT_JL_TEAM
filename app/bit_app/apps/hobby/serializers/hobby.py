from rest_framework import serializers

from bit_app.apps.hobby.models import Hobby


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = "__all__"
