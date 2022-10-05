# Generated by Django 4.1 on 2022-10-05 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventorysystem', '0003_alter_customuser_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='storageMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=50, verbose_name='Category')),
                ('ItemName', models.CharField(max_length=50, verbose_name='ItemName')),
                ('Location', models.CharField(max_length=50, verbose_name='Location')),
                ('CabinetNo', models.CharField(max_length=50, verbose_name='Cabinet')),
                ('ShelfNo', models.CharField(max_length=50, verbose_name='Shelf')),
                ('LayerNo', models.CharField(max_length=50, verbose_name='Layer')),
            ],
            options={
                'db_table': 'storageMapping',
            },
        ),
        migrations.RemoveField(
            model_name='limitrecords',
            name='limit_code',
        ),
    ]
