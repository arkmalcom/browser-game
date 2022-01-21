from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .serializers import (
    CharacterSerializer,
    EnemySerializer,
    EnemyLootSerializer,
    ItemSerializer,
    PlayerClassSerializer,
    PlayerInventorySerializer,
    UserSerializer,
)
from .models import (
    Character,
    Enemy,
    EnemyLoot,
    Item,
    PlayerClass,
    PlayerInventory,
    User,
)

# Create your views here.
class CharacterView(viewsets.ModelViewSet):
    serializer_class = CharacterSerializer
    permission_classes = (IsAdminUser,)
    queryset = Character.objects.all()