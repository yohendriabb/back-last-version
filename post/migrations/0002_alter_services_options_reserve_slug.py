# Generated by Django 5.0.6 on 2024-09-09 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name': 'Service', 'verbose_name_plural': 'Services'},
        ),
        migrations.AddField(
            model_name='reserve',
            name='slug',
            field=models.SlugField(default='red', unique=True),
        ),
    ]
