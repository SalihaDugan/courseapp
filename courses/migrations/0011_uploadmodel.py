# Generated by Django 5.1.2 on 2024-11-05 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_course_ishome_alter_course_isactive'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]