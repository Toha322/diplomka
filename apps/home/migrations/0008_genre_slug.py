# Generated by Django 5.1.4 on 2024-12-24 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_game_full_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
