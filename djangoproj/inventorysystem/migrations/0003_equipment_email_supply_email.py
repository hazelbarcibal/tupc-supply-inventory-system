# Generated by Django 4.1.3 on 2022-12-07 14:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventorysystem', '0002_remove_acceptsupplyrequests_arequest_supply_supplycabinetno_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='equipment_email',
            fields=[
                ('emailequipment_id', models.AutoField(primary_key=True, serialize=False)),
                ('emailequipment_department', models.CharField(max_length=50, unique=True, verbose_name='emailequipment_department')),
                ('emailequipment_acceptedquantity', models.CharField(max_length=50, unique=True, verbose_name='emailequipment_acceptedquantity')),
                ('current_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='current_date')),
            ],
            options={
                'db_table': 'equipment_email',
            },
        ),
        migrations.CreateModel(
            name='supply_email',
            fields=[
                ('emailsupply_id', models.AutoField(primary_key=True, serialize=False)),
                ('emailsupply_department', models.CharField(max_length=50, unique=True, verbose_name='emailsupply_department')),
                ('emailsupply_acceptedquantity', models.CharField(max_length=50, unique=True, verbose_name='emailsupply_acceptedquantity')),
                ('current_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='current_date')),
            ],
            options={
                'db_table': 'supply_email',
            },
        ),
    ]