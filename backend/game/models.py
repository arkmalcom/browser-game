from django.db import models
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def _str_(self):
        return self.email


class UserAdmin(ModelAdmin):
    list_display = ["email", "last_login", "is_staff"]
    list_filter = ("last_login", "is_staff")
    ordering = ("email",)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if email is None:
            raise TypeError("An e-mail address must be provided.")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        if email is None:
            raise TypeError("An e-mail address must be provided.")

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class PlayerClass(models.Model):
    class Meta:
        verbose_name_plural = "Player Classes"

    name = models.CharField(max_length=32, null=True)
    description = models.TextField()

    def _str_(self):
        return self.name


class Character(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=32, null=True)
    player_class = models.ForeignKey(PlayerClass, on_delete=models.CASCADE, null=True)
    HP = models.PositiveIntegerField(default=10)
    RP = models.PositiveIntegerField(default=0)
    inventory_size = models.PositiveIntegerField(default=16)

    def _str_(self):
        return self.name


class Enemy(models.Model):
    class Meta:
        verbose_name_plural = "Enemies"

    name = models.CharField(max_length=100, null=True)
    HP = models.PositiveIntegerField(default=5)
    RP = models.PositiveIntegerField(default=0)

    def _str_(self):
        return self.name


class Item(models.Model):
    EQUIPMENT = "EQ"
    TRASH = "TR"
    CONSUMABLE = "CM"
    ITEM_TYPE_CHOICES = [
        (EQUIPMENT, "Equipment"),
        (TRASH, "Vendor trash"),
        (CONSUMABLE, "Consumable"),
    ]

    name = models.CharField(max_length=100, null=True)
    description = models.TextField()
    type = models.CharField(max_length=2, choices=ITEM_TYPE_CHOICES, default=TRASH)
    unique = models.BooleanField(null=False)

    def _str_(self):
        return self.name


class PlayerInventory(models.Model):
    class Meta:
        verbose_name_plural = "Player Inventories"

    item_id = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name="player_item"
    )
    character_id = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="character"
    )


class EnemyLoot(models.Model):
    class Meta:
        verbose_name_plural = "Enemy Loot"

    item_id = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name="enemy_item"
    )
    enemy_id = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="enemy")
