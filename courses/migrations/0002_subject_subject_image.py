# Generated by Django 4.2.13 on 2024-06-13 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='subject_image',
            field=models.ImageField(default='/', upload_to='public/static/'),
        ),
    ]
