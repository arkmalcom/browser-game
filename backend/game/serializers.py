from rest_framework import serializers
from .models import (
    Character,
    Enemy,
    Item,
    PlayerClass,
    Skill,
    User,
)


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class PlayerClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerClass
        fields = "__all__"


class CharacterSerializer(serializers.ModelSerializer):
    inventory = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Character
        fields = [
            "name",
            "HP",
            "RP",
            "inventory_size",
            "user",
            "player_class",
            "inventory",
        ]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["player_class"] = instance.player_class.name
        rep["user"] = instance.user.email
        return rep


class EnemySerializer(serializers.ModelSerializer):
    loot = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Enemy
        fields = ["name", "HP", "RP", "loot"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "is_active",
        ]
        read_only_fields = ["is_active", "is_staff"]
