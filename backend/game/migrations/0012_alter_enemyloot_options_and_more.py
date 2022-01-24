# Generated by Django 4.0.1 on 2022-01-24 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0011_alter_playerinventory_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enemyloot',
            options={'verbose_name_plural': 'Enemy Loot'},
        ),
        migrations.AlterUniqueTogether(
            name='enemyloot',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='enemyloot',
            name='enemy',
            field=models.ManyToManyField(to='game.Enemy'),
        ),
        migrations.AddField(
            model_name='enemyloot',
            name='item',
            field=models.ManyToManyField(to='game.Item'),
        ),
        migrations.RemoveField(
            model_name='enemyloot',
            name='enemy_id',
        ),
        migrations.RemoveField(
            model_name='enemyloot',
            name='item_id',
        ),
    ]