from rest_framework import permissions
from rest_framework import viewsets

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


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EnemyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Enemy.objects.all()
    serializer_class = EnemySerializer


class EnemyLootViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EnemyLoot.objects.all()
    serializer_class = EnemyLootSerializer


class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class PlayerClassViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PlayerClass.objects.all()
    serializer_class = PlayerClassSerializer


class PlayerInventoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PlayerInventory.objects.all()
    serializer_class = PlayerInventorySerializer

