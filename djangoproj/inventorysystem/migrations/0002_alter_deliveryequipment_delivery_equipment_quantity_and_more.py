# Generated by Django 4.0.6 on 2022-09-09 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventorysystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryequipment',
            name='delivery_equipment_quantity',
            field=models.DecimalField(decimal_places=0, max_digits=6, verbose_name='delivery_equipment_quantity'),
        ),
        migrations.AlterField(
            model_name='deliverysupply',
            name='delivery_supply_quantity',
            field=models.DecimalField(decimal_places=0, max_digits=6, verbose_name='delivery_supply_quantity'),
        ),
    ]
