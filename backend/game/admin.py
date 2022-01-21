from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    Character,
    Enemy,
    EnemyLoot,
    Item,
    PlayerClass,
    PlayerInventory,
    User,
)

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Character)
admin.site.register(Enemy)
admin.site.register(EnemyLoot)
admin.site.register(Item)
admin.site.register(PlayerClass)
admin.site.register(PlayerInventory)
