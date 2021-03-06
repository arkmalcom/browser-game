# Generated by Django 4.0.2 on 2022-02-23 03:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[('EQ', 'Equipment'), ('TR', 'Vendor trash'), ('CM', 'Consumable')], default='TR', max_length=2)),
                ('unique', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.TextField()),
                ('cost', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, null=True)),
                ('description', models.TextField()),
                ('skills', models.ManyToManyField(to='game.Skill')),
            ],
            options={
                'verbose_name_plural': 'Player Classes',
            },
        ),
        migrations.CreateModel(
            name='Enemy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('HP', models.PositiveIntegerField(default=5)),
                ('RP', models.PositiveIntegerField(default=0)),
                ('loot', models.ManyToManyField(to='game.Item')),
            ],
            options={
                'verbose_name_plural': 'Enemies',
            },
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, null=True)),
                ('HP', models.PositiveIntegerField(default=10)),
                ('RP', models.PositiveIntegerField(default=0)),
                ('inventory_size', models.PositiveIntegerField(default=16)),
                ('inventory', models.ManyToManyField(to='game.Item')),
                ('player_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='game.playerclass')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
