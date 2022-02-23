from django.db import models
from core.models import User
from core.models import TimeStampedModel


# Create your models here.
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

    def __str__(self):
        return self.name


class Enemy(models.Model):
    class Meta:
        verbose_name_plural = "Enemies"

    name = models.CharField(max_length=100, null=True)
    HP = models.PositiveIntegerField(default=5)
    RP = models.PositiveIntegerField(default=0)
    loot = models.ManyToManyField(Item)

    def __str__(self):
        return self.name


class Skill(models.Model):

    name = models.CharField(max_length=100, null=True)
    description = models.TextField()
    cost = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class PlayerClass(models.Model):
    class Meta:
        verbose_name_plural = "Player Classes"

    name = models.CharField(max_length=32, null=True)
    description = models.TextField()
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.name


class Character(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=32, null=True)
    player_class = models.ForeignKey(PlayerClass, on_delete=models.CASCADE, null=True)
    HP = models.PositiveIntegerField(default=10)
    RP = models.PositiveIntegerField(default=0)
    inventory_size = models.PositiveIntegerField(default=16)
    inventory = models.ManyToManyField(Item)

    def __str__(self):
        return self.name
