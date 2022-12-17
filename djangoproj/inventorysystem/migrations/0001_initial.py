# Generated by Django 3.2.8 on 2022-12-17 10:45

import datetime
import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='acceptEquipmentRequests',
            fields=[
                ('acceptEquipmentRequests_id', models.AutoField(primary_key=True, serialize=False)),
                ('arequest_equipment_property_no', models.CharField(max_length=50, null=True, verbose_name='arequest_equipment_property_no')),
                ('arequest_equipment_itemname', models.CharField(max_length=255, verbose_name='arequest_equipment_itemname')),
                ('arequest_equipment_description', models.CharField(max_length=255, verbose_name='arequest_equipment_description')),
                ('arequest_equipment_brand', models.CharField(max_length=50, verbose_name='arequest_equipment_brand')),
                ('arequest_equipment_quantity', models.DecimalField(decimal_places=0, max_digits=6, verbose_name='arequest_equipment_quantity')),
                ('arequest_equipment_remaining', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='arequest_equipment_remaining')),
                ('arequest_equipment_status', models.CharField(max_length=50, verbose_name='arequest_equipment_status')),
                ('arequest_equipment_yearacquired', models.CharField(max_length=50, verbose_name='arequest_yearacquired')),
                ('arequest_equipment_issued_to', models.CharField(max_length=50, verbose_name='arequest_equipment_issued_to')),
                ('arequest_equipment_model_no', models.CharField(max_length=50, verbose_name='arequest_equipment_model_no')),
                ('arequest_equipment_serial_no', models.CharField(max_length=50, null=True, verbose_name='arequest_equipment_serial_no')),
                ('arequest_equipment_certifiedcorrect', models.CharField(max_length=50, verbose_name='arequest_equipment_certifiedcorrect')),
                ('current_date', models.DateField(default=datetime.date.today, verbose_name='arequest_current_date')),
                ('current_time', models.TimeField(auto_now_add=True, verbose_name='arequest_current_time')),
            ],
            options={
                'db_table': 'acceptEquipmentRequests',
            },
        ),
        migrations.CreateModel(
            name='acceptSupplyRequests',
            fields=[
                ('acceptSupplyRequests_id', models.AutoField(primary_key=True, serialize=False)),
                ('arequest_supply_department', models.CharField(max_length=50, verbose_name='arequest_supply_department')),
                ('arequest_supply_description', models.CharField(max_length=255, verbose_name='arequest_supply_description')),
                ('arequest_supply_unit', models.CharField(max_length=50, verbose_name='arequest_supply_unit')),
                ('arequest_supply_quantity', models.DecimalField(decimal_places=0, max_digits=6, verbose_name='arequest_supply_quantity')),
                ('arequest_supply_remaining', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='arequest_supply_remaining')),
                ('arequest_supply_status', models.CharField(max_length=50, verbose_name='arequest_supply_status')),
                ('arequest_supply_amount', models.CharField(max_length=50, verbose_name='arequest_supply_amount')),
                ('arequest_supply_requestedby', models.CharField(max_length=50, verbose_name='arequest_supply_requestedby')),
                ('current_date', models.DateField(default=datetime.date.today, verbose_name='current_date')),
                ('current_time', models.TimeField(auto_now_add=True, verbose_name='current_time')),
            ],
            options={
                'db_table': 'acceptSupplyRequests',
            },
        ),
        migrations.CreateModel(
            name='deliveryequipment',
            fields=[
                ('deliveryequipment_id', models.AutoField(primary_key=True, serialize=False)),
                ('delivery_equipment_itemname', models.CharField(max_length=50, verbose_name='delivery_equipment_itemname')),
                ('delivery_equipment_description', models.CharField(max_length=255, verbose_name='delivery_equipment_description')),
                ('delivery_equipment_brand', models.CharField(max_length=50, verbose_name='delivery_equipment_brand')),
                ('delivery_equipment_quantity', models.DecimalField(decimal_places=0, max_digits=6, verbose_name='delivery_equipment_quantity')),
                ('delivery_equipment_remaining', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='delivery_equipment_remaining')),
                ('current_date', models.DateField(default=datetime.date.today, verbose_name='delivery_current_date')),
                ('current_time', models.TimeField(auto_now_add=True, verbose_name='delivery_current_time')),
            ],
            options={
                'db_table': 'deliveryequipment',
            },
        ),
        migrations.CreateModel(
            name='deliverysupply',
            fields=[
                ('deliverysupply_id', models.AutoField(primary_key=True, serialize=False)),
                ('delivery_supply_description', models.CharField(max_length=255, verbose_name='delivery_supply_description')),
                ('delivery_supply_unit', models.CharField(max_length=50, verbose_name='delivery_supply_unit')),
                ('delivery_supply_quantity', models.DecimalField(decimal_places=0, max_digits=6, verbose_name='delivery_supply_quantity')),
                ('delivery_supply_remaining', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='delivery_supply_remaining')),
                ('delivery_supplyRackNo', models.CharField(max_length=50, null=True, verbose_name='Supply Rack')),
                ('delivery_supplyLayerNo', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='Supply Layer')),
                ('delivery_supplyCabinetNo', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='Supply Cabinet')),
                ('delivery_supplyShelfNo', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='Supply Shelf')),
                ('current_date', models.DateField(default=datetime.date.today, verbose_name='delivery_current_date')),
                ('current_time', models.TimeField(auto_now_add=True, verbose_name='delivery_current_time')),
            ],
            options={
                'db_table': 'deliverysupply',
            },
        ),
        migrations.CreateModel(
            name='department_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_form', models.FileField(null=True, upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='equipment_createform',
            fields=[
                ('createformequipment_id', models.AutoField(primary_key=True, serialize=False)),
                ('createformequipment_department', models.CharField(max_length=50, unique=True, verbose_name='createformequipment_department')),
                ('createformequipment_itemname', models.CharField(max_length=50, unique=True, verbose_name='createformequipment_itemname')),
                ('createformequipment_description', models.CharField(max_length=50, unique=True, verbose_name='createformequipment_description')),
                ('createformequipment_brand', models.CharField(max_length=50, unique=True, verbose_name='createformequipment_brand')),
                ('createformequipment_acceptedquantity', models.CharField(max_length=50, unique=True, verbose_name='createformequipment_acceptedquantity')),
                ('current_date', models.DateField(default=datetime.date.today, verbose_name='current_date')),
                ('current_time', models.TimeField(auto_now_add=True, verbose_name='current_time')),
            ],
            options={
                'db_table': 'equipment_createform',
            },
        ),
        migrations.CreateModel(
            name='equipment_disposal',
            fields=[
                ('equipmentDisposal_id', models.AutoField(primary_key=True, serialize=False)),
                ('dispose_equipment_location', models.CharField(max_length=50, null=True, verbose_name='dispose_equipment_location')),
                ('dispose_equipment_property_no', models.CharField(max_length=50, unique=True, verbose_name='dispose_equipment_property_no')),
                ('dispose_equipment_itemname', models.CharField(max_length=50, verbose_name='dispose_equipment_itemname')),
                ('dispose_equipment_description', models.CharField(max_length=255, verbose_name='dispose_equipment_description')),
                ('dispose_equipment_brand', models.CharField(max_length=50, verbose_name='dispose_equipment_brand')),
                ('dispose_equipment_yearacquired', models.CharField(max_length=50, verbose_name='dispose_yearacquired')),
                ('dispose_equipment_issued_to', models.CharField(max_length=50, verbose_name='dispose_equipment_issued_to')),
                ('dispose_equipment_model_no', models.CharField(max_length=50, verbose_name='dispose_equipment_model_no')),
                ('dispose_equipment_serial_no', models.CharField(max_length=50, unique=True, verbose_name='dispose_equipment_serial_no')),
                ('dispose_equipment_certifiedcorrect', models.CharField(max_length=50, verbose_name='dispose_equipment_certifiedcorrect')),
                ('dispose_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='dispose_date')),
            ],
            options={
                'db_table': 'equipment_disposal',
            },
        ),
        migrations.CreateModel(
            name='equipment_email',
            fields=[
                ('emailequipment_id', models.AutoField(primary_key=True, serialize=False)),
                ('emailequipment_department', models.CharField(max_length=50, unique=True, verbose_name='emailequipment_department')),
                ('emailequipment_acceptedquantity', models.CharField(max_length=50, unique=True, verbose_name='emailequipment_acceptedquantity')),
                ('current_date', models.DateField(default=datetime.date.today, verbose_name='current_date')),
                ('current_time', models.TimeField(auto_now_add=True, verbose_name='current_time')),
            ],
            options={
                'db_table': 'equipment_email',
            },
        ),
        migrations.CreateModel(
            name='equipmentmainstorage',
            fields=[
                ('equipmentmainstorage_id', models.AutoField(primary_key=True, serialize=False)),
                ('equipmentmainstorage_itemName', models.CharField(max_length=50, verbose_name='equipmentmainstorage_itemName')),
                ('equipmentmainstorage_description', models.CharField(max_length=255, verbose_name='equipmentmainstorage_description')),
                ('equipmentmainstorage_brand', models.CharField(max_length=50, verbose_name='equipmentmainstorage_brand')),
                ('equipmentmainstorage_quantity', models.DecimalField(decimal_places=0, max_digits=50, verbose_name='equipmentmainstorage_quantity')),
                ('equipmentmainstorage_remaining', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='equipmentmainstorage_remaining')),
                ('equipmentmainstorage_RequestQuantity', models.DecimalField(decimal_places=0, max_digits=50, null=True, verbose_name='equipmentmainstorage_RequestQuantity')),
            ],
            options={
                'db_table': 'equipmentmainstorage',
            },
        ),
        migrations.CreateModel(
            name='limitrecords',
            fields=[
                ('limit_id', models.AutoField(primary_key=True, serialize=False)),
                ('limit_description', models.CharField(max_length=255, verbose_name='limit_description')),
                ('limit_unit', models.CharField(max_length=50, verbose_name='limit_unit')),
                ('limit_quantity', models.DecimalField(decimal_places=0, max_digits=6, verbose_name='limit_quantity')),
                ('limit_department', models.CharField(max_length=50, verbose_name='limit_department')),
                ('limit_addquantity', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='limit_addquantity')),
                ('limit_requestedby', models.CharField(max_length=50, verbose_name='limit_requestedby')),
            ],
            options={
                'db_table': 'limitrecords',
            },
        ),
        migrations.CreateModel(
            name='requestequipment',
            fields=[
                ('requestequipment_id', models.AutoField(primary_key=True, serialize=False)),
                ('request_equipment_itemname', models.CharField(max_length=50, verbose_name='request_equipment_itemname')),
                ('request_equipment_description', models.CharField(max_length=255, verbose_name='request_equipment_description')),
                ('request_equipment_brand', models.CharField(max_length=50, verbose_name='request_equipment_brand')),
                ('request_equipment_quantity', models.DecimalField(decimal_places=0, max_digits=6, verbose_name='request_equipment_quantity')),
                ('request_equipment_department', models.CharField(max_length=50, verbose_name='request_equipment_department')),
                ('request_equipment_status', models.CharField(max_length=50, verbose_name='request_equipment_status')),
                ('request_equipment_mainstoragequantity', models.DecimalField(decimal_places=0, max_digits=6, max_length=50, null=True, verbose_name='request_equipment_mainstoragequantity')),
                ('request_equipment_acceptquantity', models.DecimalField(decimal_places=0, max_digits=6, max_length=50, null=True, verbose_name='request_equipment_acceptquantity')),
                ('current_date', models.DateField(default=datetime.date.today, verbose_name='request_current_date')),
                ('current_time', models.TimeField(auto_now_add=True, verbose_name='request_current_time')),
            ],
            options={
                'db_table': 'requestequipment',
            },
        ),
        migrations.CreateModel(
            name='requestsupply',
            fields=[
                ('requestsupply_id', models.AutoField(primary_key=True, serialize=False)),
                ('request_supply_description', models.CharField(max_length=255, verbose_name='request_supply_description')),
                ('request_supply_unit', models.CharField(max_length=50, verbose_name='request_supply_unit')),
                ('request_supply_quantity', models.DecimalField(decimal_places=0, max_digits=6, verbose_name='request_supply_quantity')),
                ('request_supply_remaining', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='request_supply_remaining')),
                ('request_supply_department', models.CharField(max_length=50, verbose_name='request_supply_department')),
                ('request_supply_status', models.CharField(max_length=50, verbose_name='request_supply_status')),
                ('request_supply_mainstoragequantity', models.DecimalField(decimal_places=0, max_digits=6, max_length=50, null=True, verbose_name='request_supply_mainstoragequantity')),
                ('request_supply_acceptquantity', models.DecimalField(decimal_places=0, max_digits=6, max_length=50, null=True, verbose_name='request_supply_acceptquantity')),
                ('request_supply_amount', models.CharField(max_length=50, verbose_name='request_supply_amount')),
                ('request_supply_requestedby', models.CharField(max_length=50, verbose_name='request_supply_requestedby')),
                ('request_supply_supplyRackNo', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='request_supply_Rack')),
                ('request_supply_supplyLayerNo', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='request_supply_Layer')),
                ('request_supply_supplyCabinetNo', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='request_supply_Cabinet')),
                ('request_supply_supplyShelfNo', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='request_supply_Shelf')),
                ('current_date', models.DateField(default=datetime.date.today, verbose_name='request_current_date')),
                ('current_time', models.TimeField(auto_now_add=True, verbose_name='request_current_time')),
            ],
            options={
                'db_table': 'requestsupply',
            },
        ),
        migrations.CreateModel(
            name='returnequipment',
            fields=[
                ('returnequipment_id', models.AutoField(primary_key=True, serialize=False)),
                ('return_equipment_location', models.CharField(max_length=50, null=True, verbose_name='return_equipment_location')),
                ('return_equipment_property_no', models.CharField(max_length=50, unique=True, verbose_name='return_equipment_property_no')),
                ('return_equipment_itemname', models.CharField(max_length=50, verbose_name='return_equipment_itemname')),
                ('return_equipment_description', models.CharField(max_length=255, verbose_name='return_equipment_description')),
                ('return_equipment_brand', models.CharField(max_length=50, verbose_name='return_equipment_brand')),
                ('return_equipment_yearacquired', models.CharField(max_length=50, verbose_name='return_yearacquired')),
                ('return_equipment_issued_to', models.CharField(max_length=50, verbose_name='return_equipment_issued_to')),
                ('return_equipment_model_no', models.CharField(max_length=50, verbose_name='return_equipment_model_no')),
                ('return_equipment_serial_no', models.CharField(max_length=50, unique=True, verbose_name='return_equipment_serial_no')),
                ('return_equipment_certifiedcorrect', models.CharField(max_length=50, verbose_name='return_equipment_certifiedcorrect')),
                ('dispose_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='return_date')),
                ('return_date', models.CharField(max_length=50, verbose_name='return_date')),
            ],
            options={
                'db_table': 'returnequipment',
            },
        ),
        migrations.CreateModel(
            name='statusEquipmentRequest',
            fields=[
                ('statusEquipmentRequests_id', models.AutoField(primary_key=True, serialize=False)),
                ('status_equipment_department', models.CharField(max_length=50, verbose_name='status_equipment_department')),
                ('status_equipment_itemname', models.CharField(max_length=255, verbose_name='status_equipment_itemname')),
                ('status_equipment_description', models.CharField(max_length=255, verbose_name='status_equipment_description')),
                ('status_equipment_brand', models.CharField(max_length=50, verbose_name='status_equipment_brand')),
                ('status_equipment_quantity', models.DecimalField(decimal_places=0, max_digits=6, verbose_name='status_equipment_quantity')),
                ('status_equipment_acceptquantity', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='status_equipment_acceptquantity')),
                ('status_equipment_remaining', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='status_equipment_remaining')),
                ('status_equipment_status', models.CharField(max_length=50, verbose_name='status_equipment_status')),
            ],
            options={
                'db_table': 'statusEquipmentRequest',
            },
        ),
        migrations.CreateModel(
            name='statusSupplyRequest',
            fields=[
                ('statusSupplyRequests_id', models.AutoField(primary_key=True, serialize=False)),
                ('status_supply_department', models.CharField(max_length=50, verbose_name='status_supply_department')),
                ('status_supply_description', models.CharField(max_length=255, verbose_name='status_supply_description')),
                ('status_supply_unit', models.CharField(max_length=50, verbose_name='status_supply_unit')),
                ('status_supply_quantity', models.DecimalField(decimal_places=0, max_digits=6, verbose_name='status_supply_quantity')),
                ('status_supply_acceptquantity', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='status_supply_acceptquantity')),
                ('status_supply_remaining', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='status_supply_remaining')),
                ('status_supply_status', models.CharField(max_length=50, verbose_name='status_supply_status')),
            ],
            options={
                'db_table': 'statusSupplyRequest',
            },
        ),
        migrations.CreateModel(
            name='supply_createform',
            fields=[
                ('createformsupply_id', models.AutoField(primary_key=True, serialize=False)),
                ('createformsupply_department', models.CharField(max_length=50, verbose_name='createformsupply_department')),
                ('createformsupply_description', models.CharField(max_length=50, verbose_name='createformsupply_description')),
                ('createformsupply_unit', models.CharField(max_length=50, verbose_name='createformsupply_unit')),
                ('createformsupply_acceptedquantity', models.CharField(max_length=50, verbose_name='createformsupply_acceptedquantity')),
                ('createformsupply_amount', models.CharField(max_length=50, verbose_name='arequest_supply_amount')),
                ('createformsupply_requestedby', models.CharField(max_length=50, verbose_name='arequest_supply_requestedby')),
                ('current_date', models.DateField(default=datetime.date.today, verbose_name='createformsupply_current_date')),
                ('current_time', models.TimeField(auto_now_add=True, verbose_name='createformsupply_current_time')),
            ],
            options={
                'db_table': 'supply_createform',
            },
        ),
        migrations.CreateModel(
            name='supply_email',
            fields=[
                ('emailsupply_id', models.AutoField(primary_key=True, serialize=False)),
                ('emailsupply_department', models.CharField(max_length=50, verbose_name='emailsupply_department')),
                ('emailsupply_acceptedquantity', models.CharField(max_length=50, verbose_name='emailsupply_acceptedquantity')),
                ('current_date', models.DateField(default=datetime.date.today, verbose_name='current_date')),
                ('current_time', models.TimeField(auto_now_add=True, verbose_name='current_time')),
            ],
            options={
                'db_table': 'supply_email',
            },
        ),
        migrations.CreateModel(
            name='supply_storagemapping',
            fields=[
                ('supplyStoragemapping_id', models.AutoField(primary_key=True, serialize=False)),
                ('supplyItemName', models.CharField(max_length=50, verbose_name='Supply ItemName')),
                ('supplyRackNo', models.CharField(max_length=50, null=True, verbose_name='Supply Rack')),
                ('supplyLayerNo', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='Supply Layer')),
                ('supplyCabinetNo', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='Supply Cabinet')),
                ('supplyShelfNo', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='Supply Shelf')),
            ],
            options={
                'db_table': 'supply_StorageMapping',
            },
        ),
        migrations.CreateModel(
            name='supplymainstorage',
            fields=[
                ('supplymainstorage_id', models.AutoField(primary_key=True, serialize=False)),
                ('supplymainstorage_description', models.CharField(max_length=255, verbose_name='supplymainstorage_description')),
                ('supplymainstorage_unit', models.CharField(max_length=50, verbose_name='supplymainstorage_unit')),
                ('supplymainstorage_quantity', models.DecimalField(decimal_places=0, max_digits=50, verbose_name='supplymainstorage_quantity')),
                ('supplymainstorage_remaining', models.DecimalField(decimal_places=0, max_digits=50, null=True, verbose_name='supplymainstorage_remaining')),
                ('supplymainstorage_RequestQuantity', models.DecimalField(decimal_places=0, max_digits=50, null=True, verbose_name='supplymainstorage_RequestQuantity')),
                ('supplymainstorage_supplyRackNo', models.CharField(max_length=50, null=True, verbose_name='Supply_Rack')),
                ('supplymainstorage_supplyLayerNo', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='Supply_Layer')),
                ('supplymainstorage_supplyCabinetNo', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='Supply_Cabinet')),
                ('supplymainstorage_supplyShelfNo', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='Supply_Shelf')),
                ('current_date', models.DateField(default=datetime.date.today, verbose_name='supplymainstorage_current_date')),
                ('current_time', models.TimeField(auto_now_add=True, verbose_name='supplymainstorage_current_time')),
            ],
            options={
                'db_table': 'supplymainstorage',
            },
        ),
        migrations.CreateModel(
            name='withdrawequipment',
            fields=[
                ('withdrawequipment_id', models.AutoField(primary_key=True, serialize=False)),
                ('withdraw_equipment_property_no', models.CharField(max_length=50, unique=True, verbose_name='withdraw_equipment_property_no')),
                ('withdraw_equipment_itemname', models.CharField(max_length=50, verbose_name='withdraw_equipment_itemname')),
                ('withdraw_equipment_description', models.CharField(max_length=255, verbose_name='withdraw_equipment_description')),
                ('withdraw_equipment_brand', models.CharField(max_length=50, verbose_name='withdraw_equipment_brand')),
                ('withdraw_equipment_yearacquired', models.CharField(max_length=50, verbose_name='withdraw_yearacquired')),
                ('withdraw_equipment_issued_to', models.CharField(max_length=50, verbose_name='withdraw_equipment_issued_to')),
                ('withdraw_equipment_model_no', models.CharField(max_length=50, unique=True, verbose_name='withdraw_equipment_model_no')),
                ('withdraw_equipment_serial_no', models.CharField(max_length=50, null=True, unique=True, verbose_name='withdraw_equipment_serial_no')),
                ('withdraw_equipment_certifiedcorrect', models.CharField(max_length=50, verbose_name='withdraw_equipment_certifiedcorrect')),
                ('current_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='withdraw_current_date')),
                ('withdraw_equipment_status', models.CharField(max_length=50, verbose_name='withdraw_equipment_status')),
            ],
            options={
                'db_table': 'withdrawequipment',
            },
        ),
        migrations.CreateModel(
            name='withdrawsupply',
            fields=[
                ('withdrawsupply_id', models.AutoField(primary_key=True, serialize=False)),
                ('withdraw_supply_department', models.CharField(max_length=50, verbose_name='withdraw_supply_department')),
                ('withdraw_supply_description', models.CharField(max_length=255, verbose_name='withdraw_supply_description')),
                ('withdraw_supply_unit', models.CharField(max_length=50, verbose_name='withdraw_supply_unit')),
                ('withdraw_supply_quantity', models.DecimalField(decimal_places=0, max_digits=6, verbose_name='withdraw_supply_quantity')),
                ('withdraw_supply_remaining', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='withdraw_supply_remaining')),
                ('withdraw_supply_supplyRackNo', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='withdraw_supply_Rack')),
                ('withdraw_supply_supplyLayerNo', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='withdraw_supply_Layer')),
                ('withdraw_supply_supplyCabinetNo', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='withdraw_supply_Cabinet')),
                ('withdraw_supply_supplyShelfNo', models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='withdraw_supply_Shelf')),
                ('current_date', models.DateField(default=datetime.date.today, verbose_name='withdraw_current_date')),
                ('current_time', models.TimeField(auto_now_add=True, verbose_name='withdraw_current_time')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(default='', max_length=30, unique=True, verbose_name='username')),
                ('department', models.CharField(max_length=250, null=True, verbose_name='department')),
                ('email', models.EmailField(default='', max_length=250, unique=True, verbose_name='email')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_department', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'inventorysystem_customuser',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
