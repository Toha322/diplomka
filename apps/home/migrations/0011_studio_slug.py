# Generated by Django 5.1.4 on 2024-12-24 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_comment_dislike_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='studio',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]