# Generated by Django 4.2.11 on 2024-05-04 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trangchu', '0018_remove_image_room_phong'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phong',
            name='Diachi_cuthe',
        ),
    ]