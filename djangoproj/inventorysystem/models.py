from django.db import models
# Create your models here.
from django.db.models import Model
from django.utils import timezone
from datetime import date
from datetime import time


class admin(models.Model):

    Admin_Username = models.CharField(max_length=50, verbose_name='admin username')
    Admin_Password = models.CharField(max_length=50, verbose_name='admin password')

def __str__(self):
    return self.Admin_Username

class deliverysupply(models.Model):

    delivery_supply_itemname = models.CharField(max_length=50, verbose_name='delivery_supply_itemname')
    delivery_supply_description = models.CharField(max_length=100, verbose_name='delivery_supply_description')
    delivery_supply_brand = models.CharField(max_length=50, verbose_name='delivery_supply_brand')
    delivery_supply_unit = models.CharField(max_length=50, verbose_name='delivery_supply_unit')
    delivery_supply_quantity = models.CharField(max_length=50, verbose_name='delivery_supply_quantity')
    delivery_supply_remaining = models.CharField(max_length=50, verbose_name='delivery_supply_remaining')
    current_date = models.DateField(default=date.today, verbose_name= 'delivery_current_date')
    #current_time = models.CharField(max_length=50, verbose_name='delivery_current_time')

    class Meta:
        db_table = ('deliverysupply')


class deliveryequipment(models.Model):

    delivery_equipment_itemname = models.CharField(max_length=50, verbose_name='delivery_equipment_itemname')
    delivery_equipment_description = models.CharField(max_length=100, verbose_name='delivery_equipment_description')
    delivery_equipment_brand = models.CharField(max_length=50, verbose_name='delivery_equipment_brand')
    delivery_equipment_unit = models.CharField(max_length=50, verbose_name='delivery_equipment_unit')
    delivery_equipment_quantity = models.CharField(max_length=50, verbose_name='delivery_equipment_quantity')
    delivery_equipment_remaining = models.CharField(max_length=50, verbose_name='delivery_equipment_remaining')
    current_date = models.DateField(default=date.today, verbose_name= 'delivery_current_date')
    #current_time = models.CharField(max_length=50, verbose_name='delivery_current_time')

    class Meta:
        db_table = ('deliveryequipment')


class requestsupply(models.Model):

    request_supply_itemname = models.CharField(max_length=50, verbose_name='request_supply_itemname')
    request_supply_description = models.CharField(max_length=100, verbose_name='request_supply_description')
    request_supply_brand = models.CharField(max_length=50, verbose_name='request_supply_brand')
    request_supply_unit = models.CharField(max_length=50, verbose_name='request_supply_unit')
    request_supply_quantity = models.CharField(max_length=50, verbose_name='request_supply_quantity')
    request_supply_department = models.CharField(max_length=50, verbose_name='request_supply_department')
    request_supply_status = models.CharField(max_length=50, verbose_name='request_supply_status')
    current_date = models.DateField(default=date.today, verbose_name= 'request_current_date')
    #current_time = models.CharField(max_length=50, verbose_name='delivery_current_time')

    class Meta:
        db_table = ('requestsupply')

class requestequipment(models.Model):

    request_equipment_itemname = models.CharField(max_length=50, verbose_name='request_equipment_itemname')
    request_equipment_description = models.CharField(max_length=100, verbose_name='request_equipment_description')
    request_equipment_brand = models.CharField(max_length=50, verbose_name='request_equipment_brand')
    request_equipment_unit = models.CharField(max_length=50, verbose_name='request_equipment_unit')
    request_equipment_quantity = models.CharField(max_length=50, verbose_name='request_equipment_quantity')
    request_equipment_department = models.CharField(max_length=50, verbose_name='request_equipment_department')
    request_equipment_status = models.CharField(max_length=50, verbose_name='request_equipment_status')
    current_date = models.DateField(default=date.today, verbose_name= 'request_current_date')
    #current_time = models.CharField(max_length=50, verbose_name='delivery_current_time')

    class Meta:
        db_table = ('requestequipment')

class withdrawsupply(models.Model):

    withdraw_supply_department = models.CharField(max_length=50, verbose_name='withdraw_supply_department')
    withdraw_supply_itemname = models.CharField(max_length=50, verbose_name='withdraw_supply_itemname')
    withdraw_supply_description = models.CharField(max_length=100, verbose_name='withdraw_supply_description')
    withdraw_supply_brand = models.CharField(max_length=50, verbose_name='withdraw_supply_brand')
    withdraw_supply_unit = models.CharField(max_length=50, verbose_name='withdraw_supply_unit')
    withdraw_supply_quantity = models.CharField(max_length=50, verbose_name='withdraw_supply_quantity')
    withdraw_supply_remaining = models.CharField(max_length=50, verbose_name='withdraw_supply_remaining')
    current_date = models.DateField(default=date.today, verbose_name='withdraw_current_date')
    withdraw_supply_status = models.CharField(max_length=50, verbose_name='withdraw_supply_status')
    class Meta:
        db_table = "withdrawsupply"


class withdrawequipment(models.Model):

    withdraw_equipment_property_no. = models.CharField(max_length=50, verbose_name='withdraw_equipment_property_no.')
    withdraw_equipment_itemname = models.CharField(max_length=50, verbose_name='withdraw_equipment_itemname')
    withdraw_equipment_description = models.CharField(max_length=100, verbose_name='withdraw_equipment_description')
    withdraw_equipment_brand = models.CharField(max_length=50, verbose_name='withdraw_equipment_brand')
    withdraw_equipment_yearacquired = models.CharField(max_length=50, verbose_name='withdraw_yearacquired')
    withdraw_equipment_issued_to. = models.CharField(max_length=50, verbose_name='withdraw_equipment_issued_to.')
    withdraw_equipment_model_no. = models.CharField(max_length=50, verbose_name='withdraw_equipment_model_no.')
    withdraw_equipment_serial_no. = models.CharField(max_length=50, verbose_name='withdraw_equipment_serial_no.')
    withdraw_equipment_certifiedcorrect = models.CharField(max_length=50, verbose_name='withdraw_equipment_certifiedcorrect')
    current_date = models.DateField(default=date.today, verbose_name='withdraw_current_date')
    
    class Meta:
        db_table = "withdrawequipment"


class returnequipment(models.Model):

    return_equipment_property_no. = models.CharField(max_length=50, verbose_name='return_equipment_property_no.')
    return_equipment_itemname = models.CharField(max_length=50, verbose_name='return_equipment_itemname')
    return_equipment_description = models.CharField(max_length=100, verbose_name='return_equipment_description')
    return_equipment_brand = models.CharField(max_length=50, verbose_name='return_equipment_brand')
    return_equipment_yearacquired = models.CharField(max_length=50, verbose_name='return_yearacquired')
    return_equipment_issued_to. = models.CharField(max_length=50, verbose_name='return_equipment_issued_to.')
    return_equipment_model_no. = models.CharField(max_length=50, verbose_name='return_equipment_model_no.')
    return_equipment_serial_no. = models.CharField(max_length=50, verbose_name='return_equipment_serial_no.')
    return_equipment_certifiedcorrect = models.CharField(max_length=50, verbose_name='return_equipment_certifiedcorrect')
    return_date = models.DateField(default=date.today, verbose_name='return_date')
    
    class Meta:
        db_table = "returnequipment"

def __str__(self):
    return self.withdraw_item_name

class limitrecords(models.Model):

    limit_id = models.AutoField(primary_key=True)
    limit_item_name = models.CharField(max_length=50, verbose_name='limit_item_name')
    limit_description = models.CharField(max_length=50, verbose_name='limit_description')
    limit_brand = models.CharField(max_length=50, verbose_name='limit_brand')
    limit_unit = models.CharField(max_length=50, verbose_name='limit_unit')
    limit_quantity = models.CharField(max_length=50, verbose_name='limit_quantity')
    limit_department = models.CharField(max_length=50, verbose_name='limit_department')
    limit_code = models.CharField(max_length=50, verbose_name='limit_code')
    
    #current_time = models.CharField(max_length=50, verbose_name='delivery_current_time')

    class Meta:
        db_table = ('limitrecords')

class supplymainstorage(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='ItemName')
    Description = models.CharField(max_length=50, verbose_name='Description')
    Brand = models.CharField(max_length=50, verbose_name='Brand')
    Unit = models.CharField(max_length=50, verbose_name='Unit')
    Remaining = models.CharField(max_length=50, verbose_name='Remaining')

    class Meta:
        db_table = "supplymainstorage"

class equipmentmainstorage(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='ItemName')
    Description = models.CharField(max_length=50, verbose_name='Description')
    Brand = models.CharField(max_length=50, verbose_name='Brand')
    Unit = models.CharField(max_length=50, verbose_name='Unit')
    Remaining = models.CharField(max_length=50, verbose_name='Remaining')

    class Meta:
        db_table = "equipmentmainstorage"

