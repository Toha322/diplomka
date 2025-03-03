# Generated by Django 5.1.4 on 2024-12-26 13:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_studio_slug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GameLibrary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_library', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Библиотека пользователя',
                'verbose_name_plural': 'Библиотеки пользователей',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='GameLibraryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_downloaded', models.BooleanField(default=False, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.game', verbose_name='Игра')),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_library_items', to='home.gamelibrary', verbose_name='Библиотека')),
            ],
            options={
                'verbose_name': 'Игра в библиотеке',
                'verbose_name_plural': 'Игры в библиотеке',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='WishLibrary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wish_library', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Библиотека пользователя',
                'verbose_name_plural': 'Библиотеки пользователей',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='WishLibraryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_downloaded', models.BooleanField(default=False, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.game', verbose_name='Игра')),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wish_library_items', to='home.wishlibrary', verbose_name='Библиотека')),
            ],
            options={
                'verbose_name': 'Игра в библиотеке',
                'verbose_name_plural': 'Игры в библиотеке',
                'ordering': ['-updated_at'],
            },
        ),
    ]
