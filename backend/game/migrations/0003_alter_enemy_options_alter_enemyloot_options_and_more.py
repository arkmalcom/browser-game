# Generated by Django 4.0.1 on 2022-01-21 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_enemy_item_playerclass_character_hp_character_rp_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enemy',
            options={'verbose_name_plural': 'Enemies'},
        ),
        migrations.AlterModelOptions(
            name='enemyloot',
            options={'verbose_name_plural': 'Enemy Loot'},
        ),
        migrations.AlterModelOptions(
            name='playerclass',
            options={'verbose_name_plural': 'Player Classes'},
        ),
        migrations.AlterModelOptions(
            name='playerinventory',
            options={'verbose_name_plural': 'Player Inventories'},
        ),
    ]