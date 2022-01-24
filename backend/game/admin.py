from django.contrib import admin
from .models import (
    Character,
    Enemy,
    Item,
    PlayerClass,
    Skill,
    User,
    UserAdmin,
)

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Character)
admin.site.register(Enemy)
admin.site.register(Item)
admin.site.register(PlayerClass)
admin.site.register(Skill)