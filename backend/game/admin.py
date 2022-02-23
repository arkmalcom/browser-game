from django.contrib import admin
from .models import (
    Character,
    Enemy,
    Item,
    PlayerClass,
    Skill,
)

# Register your models here.
@admin.register(Character)
class UserAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "created", "player_class")
    list_filter = ("created", "user",)
    readonly_fields = ("created",)
    ordering = ("user",)

admin.site.register(Enemy)
admin.site.register(Item)
admin.site.register(PlayerClass)
admin.site.register(Skill)
