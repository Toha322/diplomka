# Generated by Django 5.1.4 on 2024-12-24 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_game_options_remove_game_genre_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='description',
        ),
        migrations.AddField(
            model_name='game',
            name='full_description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='game',
            name='short_description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
