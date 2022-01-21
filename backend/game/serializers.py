from rest_framework import serializers
from .models import (
    Character,
    Enemy,
    EnemyLoot,
    Item,
    PlayerClass,
    PlayerInventory,
    User,
)


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = "__all__"


class EnemySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enemy
        fields = "__all__"


class EnemyLootSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnemyLoot
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class PlayerClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerClass
        fields = "__all__"


class PlayerInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerInventory
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
