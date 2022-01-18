from rest_framework import serializers
from .models import RandomUUID


class RandomUUIDSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    timestamp = serializers.DateTimeField()

    def to_representation(self, instance):
        response = super().to_representation(instance)
        return {response['timestamp']: response['id']}