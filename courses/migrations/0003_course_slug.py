# Generated by Django 5.1.2 on 2024-11-01 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
