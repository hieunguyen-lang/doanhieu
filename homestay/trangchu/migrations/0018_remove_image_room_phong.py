# Generated by Django 4.2.11 on 2024-05-04 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trangchu', '0017_remove_giohang_items_giohang_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image_room',
            name='phong',
        ),
    ]
