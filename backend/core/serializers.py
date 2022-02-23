from rest_framework import serializers
from core.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "is_active",
            "created",
            "modified",
        ]
        read_only_fields = ["is_active", "is_staff"]
