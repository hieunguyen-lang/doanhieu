# Generated by Django 5.0.4 on 2024-05-10 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trangchu', '0024_order_order_item_delete_room_booked_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_order',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]