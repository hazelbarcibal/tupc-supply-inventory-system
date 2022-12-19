# Generated by Django 3.1.14 on 2022-12-19 02:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventorysystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='supply_createform_inputs',
            fields=[
                ('createformsupply_inputs_id', models.AutoField(primary_key=True, serialize=False)),
                ('createformsupply_inputs_department', models.CharField(max_length=50, verbose_name='createformsupply_inputs_department')),
                ('createformsupply_inputs_description', models.CharField(max_length=50, verbose_name='createformsupply_inputs_description')),
                ('createformsupply_inputs_unit', models.CharField(max_length=50, verbose_name='createformsupply_inputs_unit')),
                ('createformsupply_inputs_acceptedquantity', models.CharField(max_length=50, verbose_name='createformsupply_inputs_acceptedquantity')),
                ('createformsupply_inputs_amount', models.CharField(max_length=50, verbose_name=' createformsupply_inputs_amount')),
                ('createformsupply_inputs_office', models.CharField(max_length=255, verbose_name=' createformsupply_inputs_office')),
                ('createformsupply_inputs_requestedby', models.CharField(max_length=50, verbose_name=' createformsupply_inputs_requestedby')),
                ('createformsupply_inputs_approvedby', models.CharField(max_length=50, verbose_name=' createformsupply_inputs_approvedby')),
                ('createformsupply_inputs_issued_by', models.CharField(max_length=50, verbose_name='createformsupply_inputs_issued_by')),
                ('createformsupply_inputs_purpose', models.CharField(max_length=255, verbose_name=' createformsupply_inputs_purpose')),
                ('current_date', models.DateField(default=datetime.date.today, verbose_name='createformsupply_inputs_current_date')),
                ('current_time', models.TimeField(auto_now_add=True, verbose_name='createformsupply_inputs_current_time')),
            ],
            options={
                'db_table': 'supply_createform_inputs',
            },
        ),
        migrations.AlterField(
            model_name='supply_createform',
            name='createformsupply_amount',
            field=models.CharField(max_length=50, verbose_name='createformsupply_amount'),
        ),
        migrations.AlterField(
            model_name='supply_createform',
            name='createformsupply_requestedby',
            field=models.CharField(max_length=50, verbose_name='createformsupply_requestedby'),
        ),
    ]
