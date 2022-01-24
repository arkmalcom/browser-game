from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializers import (
    CharacterSerializer,
    EnemySerializer,
    ItemSerializer,
    PlayerClassSerializer,
    SkillSerializer,
    UserSerializer,
)

from .models import (
    Character,
    Enemy,
    Item,
    PlayerClass,
    Skill,
    User,
)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EnemyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Enemy.objects.all()
    serializer_class = EnemySerializer


class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class PlayerClassViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PlayerClass.objects.all()
    serializer_class = PlayerClassSerializer