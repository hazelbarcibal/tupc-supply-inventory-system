# Generated by Django 3.2.8 on 2023-01-06 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventorysystem', '0003_alter_requestequipment_request_equipment_unitcost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestequipment',
            name='request_equipment_totalcost',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=6, verbose_name='request_equipment_totalcost'),
        ),
        migrations.AlterField(
            model_name='requestequipment',
            name='request_equipment_unitcost',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=6, verbose_name='request_equipment_unitcost'),
        ),
    ]
