# Generated by Django 5.0.6 on 2024-09-10 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_reserve_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='doctor',
            field=models.ManyToManyField(to='post.doctor'),
        ),
    ]
