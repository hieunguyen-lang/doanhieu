# Generated by Django 5.0.4 on 2024-05-10 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trangchu', '0025_order_number_alter_order_date_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
