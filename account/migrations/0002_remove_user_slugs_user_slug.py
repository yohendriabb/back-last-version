# Generated by Django 5.0.6 on 2024-09-09 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='slugs',
        ),
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(default='red'),
        ),
    ]
