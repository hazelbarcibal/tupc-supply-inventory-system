from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser  
from django.utils.timezone import now
from datetime import date
from datetime import time


class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, verbose_name='username', unique=True, default='')
    department = models.CharField(max_length=250, verbose_name='department', null=True)
    email = models.EmailField(max_length=250, verbose_name='email', unique=True, default='')
    is_admin = models.BooleanField(default=False)
    is_department = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.department
    

    class Meta:
        db_table = ('inventorysystem_customuser')


class department_form(models.Model):
    dep_form = models.FileField(null = True, upload_to='media')


#-------------- SUPPLY MODELS -------------------
class deliverysupply(models.Model):

    deliverysupply_id = models.AutoField(primary_key=True)
    delivery_supply_description = models.CharField(max_length=255, verbose_name='delivery_supply_description')
    delivery_supply_unit = models.CharField(max_length=50, verbose_name='delivery_supply_unit')
    delivery_supply_quantity = models.DecimalField(max_digits=6, decimal_places= 0, verbose_name='delivery_supply_quantity')
    delivery_supply_remaining = models.DecimalField(null=True, max_digits=6, decimal_places= 0, verbose_name='delivery_supply_remaining')
    delivery_supplyRackNo = models.CharField(null= True, max_length=50, verbose_name='Supply Rack')
    delivery_supplyLayerNo = models.DecimalField(null= True, max_digits=6, decimal_places=0, verbose_name='Supply Layer')
    delivery_supplyCabinetNo = models.DecimalField(null= True, max_digits=6, decimal_places=0, verbose_name='Supply Cabinet')
    delivery_supplyShelfNo = models.DecimalField(null= True, max_digits=6, decimal_places=0, verbose_name='Supply Shelf')
    current_date = models.DateField(default=date.today, verbose_name= 'delivery_current_date')
    current_time = models.TimeField(auto_now_add=True, blank=True, verbose_name= 'delivery_current_time')


    class Meta:
        db_table = ('deliverysupply')

class requestsupply(models.Model):

    requestsupply_id = models.AutoField(primary_key=True)
    request_supply_description = models.CharField(max_length=255, verbose_name='request_supply_description')
    request_supply_unit = models.CharField(max_length=50, verbose_name='request_supply_unit')
    request_supply_quantity = models.DecimalField(max_digits=6,decimal_places=0, verbose_name='request_supply_quantity')
    request_supply_remaining = models.DecimalField(null=True, max_digits=6,decimal_places=0, verbose_name='request_supply_remaining')
    request_supply_department = models.CharField(max_length=50, verbose_name='request_supply_department')
    request_supply_status = models.CharField(max_length=50, verbose_name='request_supply_status')
    request_supply_mainstoragequantity = models.DecimalField(null=True, max_digits=6, decimal_places=0, max_length=50, verbose_name='request_supply_mainstoragequantity')
    request_supply_acceptquantity = models.DecimalField(null=True, max_digits=6, decimal_places=0, max_length=50, verbose_name='request_supply_acceptquantity')
    request_supply_amount = models.CharField(max_length=50, verbose_name='request_supply_amount')
    request_supply_supplyRackNo = models.DecimalField(null= True, max_digits=6, decimal_places=0, verbose_name='request_supply_Rack')
    request_supply_supplyLayerNo = models.DecimalField(null= True, max_digits=6, decimal_places=0, verbose_name='request_supply_Layer')
    request_supply_supplyCabinetNo = models.DecimalField(null= True, max_digits=6, decimal_places=0, verbose_name='request_supply_Cabinet')
    request_supply_supplyShelfNo = models.DecimalField(null= True, max_digits=6, decimal_places=0, verbose_name='request_supply_Shelf')
    request_supply_daterequested = models.CharField(null= True,max_length=50, verbose_name='request_supply_daterequested')
    request_supply_dateaccepted = models.CharField(null= True,max_length=50, verbose_name='request_supply_dateaccepted')

    class Meta:
        db_table = ('requestsupply')

class withdrawsupply(models.Model):

    withdrawsupply_id = models.AutoField(primary_key=True)
    withdraw_supply_department = models.CharField(max_length=50, verbose_name='withdraw_supply_department')
    withdraw_supply_description = models.CharField(max_length=255, verbose_name='withdraw_supply_description')
    withdraw_supply_unit = models.CharField(max_length=50, verbose_name='withdraw_supply_unit')
    withdraw_supply_quantity = models.DecimalField(max_digits=6, decimal_places=0, verbose_name='withdraw_supply_quantity')
    withdraw_supply_remaining = models.DecimalField(null=True, max_digits=6, decimal_places=0, verbose_name='withdraw_supply_remaining')
    withdraw_supply_supplyRackNo = models.DecimalField(null= True, max_digits=6, decimal_places=0, verbose_name='withdraw_supply_Rack')
    withdraw_supply_supplyLayerNo = models.DecimalField(null= True, max_digits=6, decimal_places=0, verbose_name='withdraw_supply_Layer')
    withdraw_supply_supplyCabinetNo = models.DecimalField(null= True, max_digits=6, decimal_places=0, verbose_name='withdraw_supply_Cabinet')
    withdraw_supply_supplyShelfNo = models.DecimalField(null= True, max_digits=6, decimal_places=0, verbose_name='withdraw_supply_Shelf')
    # current_date = models.DateTimeField(default=now, verbose_name='withdraw_current_date')
    withdraw_supply_current_date = models.DateField(default=date.today, verbose_name= 'withdraw_current_date')
    withdraw_supply_current_time = models.TimeField(auto_now_add=True, blank=True, verbose_name= 'withdraw_current_time')

    db_table = "withdrawsupply"

class limitrecords(models.Model):

    limit_id = models.AutoField(primary_key=True)
    limit_description = models.CharField(max_length=255, verbose_name='limit_description')
    limit_unit = models.CharField(max_length=50, verbose_name='limit_unit')
    limit_quantity = models.DecimalField(max_digits=6, decimal_places=0, verbose_name='limit_quantity')
    limit_department = models.CharField(max_length=50, verbose_name='limit_department')
    limit_addquantity = models.DecimalField(null=True, max_digits=6, decimal_places=0, verbose_name='limit_addquantity')
    limit_requestedby = models.CharField(max_length=50, verbose_name='limit_requestedby')

    class Meta:
        db_table = ('limitrecords')

class supplymainstorage(models.Model):

    supplymainstorage_id = models.AutoField(primary_key=True)
    supplymainstorage_description = models.CharField(max_length=255, verbose_name='supplymainstorage_description')
    supplymainstorage_unit = models.CharField(max_length=50, verbose_name='supplymainstorage_unit')
    supplymainstorage_quantity = models.DecimalField(max_digits=50, decimal_places=0, verbose_name='supplymainstorage_quantity')
    supplymainstorage_remaining = models.DecimalField(null=True, max_digits=50, decimal_places=0, verbose_name='supplymainstorage_remaining')
    supplymainstorage_RequestQuantity = models.DecimalField(null=True, max_digits=50, decimal_places=0, verbose_name='supplymainstorage_RequestQuantity')
    supplymainstorage_supplyRackNo = models.CharField(null= True, max_length=50, verbose_name='Supply_Rack')
    supplymainstorage_supplyLayerNo = models.DecimalField(null= True, max_digits=6, decimal_places=0, verbose_name='Supply_Layer')
    supplymainstorage_supplyCabinetNo = models.DecimalField(null= True, max_digits=6, decimal_places=0, verbose_name='Supply_Cabinet')
    supplymainstorage_supplyShelfNo = models.DecimalField(null= True, max_digits=6, decimal_places=0, verbose_name='Supply_Shelf')
    # current_date = models.DateTimeField(default=now, verbose_name='supplymainstorage_current_date')
    
    
    class Meta:
        db_table = "supplymainstorage"

class acceptSupplyRequests(models.Model):

    acceptSupplyRequests_id = models.AutoField(primary_key=True)
    arequest_supply_department = models.CharField(max_length=50, verbose_name='arequest_supply_department')
    arequest_supply_description = models.CharField(max_length=255, verbose_name='arequest_supply_description')
    arequest_supply_unit = models.CharField(max_length=50, verbose_name='arequest_supply_unit')
    arequest_supply_quantity = models.DecimalField(max_digits=6,decimal_places=0, verbose_name='arequest_supply_quantity')
    arequest_supply_remaining = models.DecimalField(null=True, max_digits=6,decimal_places=0, verbose_name='arequest_supply_remaining')
    arequest_supply_status = models.CharField(max_length=50, verbose_name='arequest_supply_status')
    arequest_supply_amount = models.CharField(max_length=50, verbose_name='arequest_supply_amount')
    arequest_supply_RackNo = models.CharField(null= True, max_length=50, verbose_name='Supply_Rack')
    arequest_supply_LayerNo = models.DecimalField(null= True, max_digits=6, decimal_places=0, verbose_name='Supply_Layer')
    arequest_supply_CabinetNo = models.DecimalField(null= True, max_digits=6, decimal_places=0, verbose_name='Supply_Cabinet')
    arequest_supply_ShelfNo = models.DecimalField(null= True, max_digits=6, decimal_places=0, verbose_name='Supply_Shelf')
    # current_date = models.CharField(max_length=50, verbose_name='currentdate')
    arequest_supply_daterequested = models.CharField(null= True,max_length=50, verbose_name='arequest_supply_daterequested')
    arequest_supply_dateaccepted =  models.CharField(null= True,max_length=50, verbose_name='arequest_supply_dateaccepted')

    class Meta:
        db_table = ('acceptSupplyRequests')

class statusSupplyRequest(models.Model):

    statusSupplyRequests_id = models.AutoField(primary_key=True)
    status_supply_department = models.CharField(max_length=50, verbose_name='status_supply_department')
    status_supply_description = models.CharField(max_length=255, verbose_name='status_supply_description')
    status_supply_unit = models.CharField(max_length=50, verbose_name='status_supply_unit')
    status_supply_quantity = models.DecimalField(max_digits=6,decimal_places=0, verbose_name='status_supply_quantity')
    status_supply_acceptquantity = models.DecimalField(null=True, max_digits=6,decimal_places=0, verbose_name='status_supply_acceptquantity')
    status_supply_remaining = models.DecimalField(null=True, max_digits=6,decimal_places=0, verbose_name='status_supply_remaining')
    status_supply_status = models.CharField(max_length=50, verbose_name='status_supply_status')
    date_requested = models.CharField(null= True,max_length=50, verbose_name='date_requested')
    date_accepted =  models.CharField(null= True,max_length=50, verbose_name='date_accepted')

    class Meta:
        db_table = ('statusSupplyRequest')


#-------------- EQUIPMENT MODELS -------------------
class deliveryequipment(models.Model):

    deliveryequipment_id = models.AutoField(primary_key=True)
    delivery_equipment_itemname = models.CharField(max_length=50, verbose_name='delivery_equipment_itemname')
    delivery_equipment_description = models.CharField(max_length=255, verbose_name='delivery_equipment_description')
    delivery_equipment_brand = models.CharField(max_length=50, verbose_name='delivery_equipment_brand')
    delivery_equipment_quantity = models.DecimalField(max_digits=6, decimal_places= 0, verbose_name='delivery_equipment_quantity')
    delivery_equipment_remaining = models.DecimalField(null=True, max_digits=6, decimal_places= 0, verbose_name='delivery_equipment_remaining')
    # current_date = models.DateTimeField(default=now, editable=False, verbose_name= 'delivery_current_date')
    current_date = models.DateField(default=date.today, verbose_name= 'delivery_current_date')
    current_time = models.TimeField(auto_now_add=True, blank=True, verbose_name= 'delivery_current_time')

    class Meta:
        db_table = ('deliveryequipment')

class requestequipment(models.Model):

    requestequipment_id = models.AutoField(primary_key=True)
    request_equipment_itemname = models.CharField(max_length=50, verbose_name='request_equipment_itemname')
    request_equipment_description = models.CharField(max_length=255, verbose_name='request_equipment_description')
    request_equipment_brand = models.CharField(max_length=50, verbose_name='request_equipment_brand')
    request_equipment_unit = models.CharField(null=True,max_length=50, verbose_name='request_equipment_brand')
    request_equipment_quantity = models.DecimalField(max_digits=6, decimal_places=0, verbose_name='request_equipment_quantity')
    request_equipment_unitcost = models.DecimalField(null=True,max_digits=6, decimal_places=0, verbose_name='request_equipment_unitcost')
    request_equipment_totalcost = models.DecimalField(null=True,max_digits=6, decimal_places=0, verbose_name='request_equipment_totalcost')
    request_equipment_iin = models.CharField(null=True,max_length=50, blank=True, verbose_name='request_equipment_iin')
    request_equipment_department = models.CharField(max_length=50, verbose_name='request_equipment_department')
    request_equipment_status = models.CharField(max_length=50, verbose_name='request_equipment_status')
    request_equipment_mainstoragequantity = models.DecimalField(null=True, max_digits=6, decimal_places=0, max_length=50, verbose_name='request_equipment_mainstoragequantity')
    request_equipment_acceptquantity = models.DecimalField(null=True, max_digits=6, decimal_places=0, max_length=50, verbose_name='request_equipment_acceptquantity')
    # current_date = models.DateTimeField(default=now, verbose_name= 'request_current_date')
    request_equipment_daterequested = models.CharField(null= True,max_length=50, verbose_name='request_equipment_daterequested')
    request_equipment_dateaccepted =  models.CharField(null= True,max_length=50, verbose_name='request_equipment_dateaccepted')

    class Meta:
        db_table = ('requestequipment')

class acceptEquipmentRequests(models.Model):

    arequest_equipment_id = models.AutoField(primary_key=True)
    arequest_equipment_property_no = models.CharField(max_length=50, verbose_name='arequest_equipment_property_no')
    arequest_equipment_itemname = models.CharField(max_length=255, verbose_name='arequest_equipment_itemname')
    arequest_equipment_description = models.CharField(max_length=255, verbose_name='arequest_equipment_description')
    arequest_equipment_brand = models.CharField(max_length=50, verbose_name='arequest_equipment_brand')
    arequest_equipment_quantity = models.DecimalField(max_digits=6,decimal_places=0, verbose_name='arequest_equipment_quantity')
    arequest_equipment_remaining = models.DecimalField(max_digits=6,decimal_places=0, verbose_name='arequest_equipment_remaining')
    arequest_equipment_status = models.CharField(max_length=50, verbose_name='arequest_equipment_status')
    arequest_equipment_yearacquired = models.CharField(max_length=50, verbose_name='arequest_yearacquired')
    arequest_equipment_issued_to = models.CharField(max_length=50, verbose_name='arequest_equipment_issued_to')
    arequest_equipment_model_no = models.CharField(max_length=50, verbose_name='arequest_equipment_model_no')
    arequest_equipment_serial_no = models.CharField(null = True, max_length=50, verbose_name='arequest_equipment_serial_no')
    arequest_equipment_certifiedcorrect = models.CharField(max_length=50, verbose_name='arequest_equipment_certifiedcorrect')
    # current_date = models.DateTimeField(default=now, verbose_name= 'arequest_current_date')
    arequest_equipment_daterequested = models.CharField(null= True,max_length=50, verbose_name='arequest_equipment_daterequested')
    arequest_equipment_dateaccepted =  models.CharField(null= True,max_length=50, verbose_name='arequest_equipment_dateaccepted')

    class Meta:
        db_table = ('acceptEquipmentRequests')

class withdrawequipment(models.Model):

    withdrawequipment_id = models.AutoField(primary_key=True)
    withdraw_equipment_property_no = models.CharField(unique = True, max_length=50, verbose_name='withdraw_equipment_property_no')
    withdraw_equipment_itemname = models.CharField(max_length=50, verbose_name='withdraw_equipment_itemname')
    withdraw_equipment_description = models.CharField(max_length=255, verbose_name='withdraw_equipment_description')
    withdraw_equipment_brand = models.CharField(max_length=50, verbose_name='withdraw_equipment_brand')
    withdraw_equipment_yearacquired = models.CharField(max_length=50, verbose_name='withdraw_yearacquired')
    withdraw_equipment_issued_to = models.CharField(max_length=50, verbose_name='withdraw_equipment_issued_to')
    withdraw_equipment_model_no = models.CharField(unique = True, max_length=50, verbose_name='withdraw_equipment_model_no')
    withdraw_equipment_serial_no = models.CharField(unique = True, null = True, max_length=50, verbose_name='withdraw_equipment_serial_no')
    withdraw_equipment_certifiedcorrect = models.CharField(max_length=50, verbose_name='withdraw_equipment_certifiedcorrect')
    withdraw_equipment_current_date = models.DateTimeField(default=now, verbose_name='withdraw_current_date')
    withdraw_equipment_current_time = models.TimeField(auto_now_add=True, blank=True, verbose_name= 'withdraw_current_time')
    withdraw_equipment_status = models.CharField(max_length=50, verbose_name='withdraw_equipment_status')
    
    class Meta:
        db_table = "withdrawequipment"

class returnequipment(models.Model):

    returnequipment_id = models.AutoField(primary_key=True)
    return_equipment_location = models.CharField(null = True, max_length=50, verbose_name='return_equipment_location')
    return_equipment_property_no = models.CharField(unique=True, max_length=50, verbose_name='return_equipment_property_no')
    return_equipment_itemname = models.CharField(max_length=50, verbose_name='return_equipment_itemname')
    return_equipment_description = models.CharField(max_length=255, verbose_name='return_equipment_description')
    return_equipment_brand = models.CharField(max_length=50, verbose_name='return_equipment_brand')
    return_equipment_yearacquired = models.CharField(max_length=50, verbose_name='return_yearacquired')
    return_equipment_issued_to = models.CharField(max_length=50, verbose_name='return_equipment_issued_to')
    return_equipment_model_no = models.CharField(max_length=50, verbose_name='return_equipment_model_no')
    return_equipment_serial_no = models.CharField(unique=True, max_length=50, verbose_name='return_equipment_serial_no')
    return_equipment_certifiedcorrect = models.CharField(max_length=50, verbose_name='return_equipment_certifiedcorrect')
    dispose_date = models.DateTimeField(default=now, verbose_name='return_date')
    return_date = models.CharField(max_length=50, verbose_name='return_date')
    
    class Meta:
        db_table = "returnequipment"

def __str__(self):
    return self.withdraw_item_name

class statusEquipmentRequest(models.Model):

    statusEquipmentRequests_id = models.AutoField(primary_key=True)
    status_equipment_department = models.CharField(max_length=50, verbose_name='status_equipment_department')
    status_equipment_itemname = models.CharField(max_length=255, verbose_name='status_equipment_itemname')
    status_equipment_description = models.CharField(max_length=255, verbose_name='status_equipment_description')
    status_equipment_brand = models.CharField(max_length=50, verbose_name='status_equipment_brand')
    status_equipment_quantity = models.DecimalField(max_digits=6,decimal_places=0, verbose_name='status_equipment_quantity')
    status_equipment_acceptquantity = models.DecimalField(null=True, max_digits=6,decimal_places=0, verbose_name='status_equipment_acceptquantity')
    status_equipment_remaining = models.DecimalField(null=True, max_digits=6,decimal_places=0, verbose_name='status_equipment_remaining')
    status_equipment_status = models.CharField(max_length=50, verbose_name='status_equipment_status')
    status_equipment_daterequested = models.CharField(null= True,max_length=50, verbose_name='arequest_equipment_daterequested')
    status_equipment_dateaccepted =  models.CharField(null= True,max_length=50, verbose_name='arequest_equipment_dateaccepted')

    class Meta:
        db_table = ('statusEquipmentRequest')


class equipmentmainstorage(models.Model):

    equipmentmainstorage_id = models.AutoField(primary_key=True)
    equipmentmainstorage_itemName = models.CharField(max_length=50, verbose_name='equipmentmainstorage_itemName')
    equipmentmainstorage_description = models.CharField(max_length=255, verbose_name='equipmentmainstorage_description')
    equipmentmainstorage_brand = models.CharField(max_length=50, verbose_name='equipmentmainstorage_brand')
    equipmentmainstorage_quantity = models.DecimalField(max_digits=50, decimal_places=0, verbose_name='equipmentmainstorage_quantity')
    equipmentmainstorage_remaining = models.DecimalField(null= True, max_digits=6, decimal_places=0, verbose_name='equipmentmainstorage_remaining')
    equipmentmainstorage_RequestQuantity = models.DecimalField(null= True, max_digits=50, decimal_places=0, verbose_name='equipmentmainstorage_RequestQuantity')

    class Meta:
        db_table = "equipmentmainstorage"


#-------------- STORAGE MODELS -------------------
class supply_storagemapping(models.Model):

    supplyStoragemapping_id = models.AutoField(primary_key=True)
    supplyItemName = models.CharField(max_length=50, verbose_name='Supply ItemName')
    supplyRackNo = models.CharField(null= True, max_length=50, verbose_name='Supply Rack')
    supplyLayerNo = models.DecimalField(null= True, max_digits=6, decimal_places=0, verbose_name='Supply Layer')
    supplyCabinetNo = models.DecimalField(null= True, max_digits=6, decimal_places=0, verbose_name='Supply Cabinet')
    supplyShelfNo = models.DecimalField(null= True, max_digits=6, decimal_places=0, verbose_name='Supply Shelf')

    class Meta:
        db_table = "supply_StorageMapping"

class equipment_disposal(models.Model):

    equipmentDisposal_id = models.AutoField(primary_key=True)
    dispose_equipment_location = models.CharField(null=True, max_length=50, verbose_name='dispose_equipment_location')
    dispose_equipment_property_no = models.CharField(unique=True, max_length=50, verbose_name='dispose_equipment_property_no')
    dispose_equipment_itemname = models.CharField(max_length=50, verbose_name='dispose_equipment_itemname')
    dispose_equipment_description = models.CharField(max_length=255, verbose_name='dispose_equipment_description')
    dispose_equipment_brand = models.CharField(max_length=50, verbose_name='dispose_equipment_brand')
    dispose_equipment_yearacquired = models.CharField(max_length=50, verbose_name='dispose_yearacquired')
    dispose_equipment_issued_to = models.CharField(max_length=50, verbose_name='dispose_equipment_issued_to')
    dispose_equipment_model_no = models.CharField(max_length=50, verbose_name='dispose_equipment_model_no')
    dispose_equipment_serial_no = models.CharField(unique=True, max_length=50, verbose_name='dispose_equipment_serial_no')
    dispose_equipment_certifiedcorrect = models.CharField(max_length=50, verbose_name='dispose_equipment_certifiedcorrect')
    dispose_date = models.DateTimeField(default=now, verbose_name='dispose_date')



    class Meta:
        db_table = "equipment_disposal"

class equipment_disposed(models.Model):

    equipmentDisposed_id = models.AutoField(primary_key=True)
    disposed_equipment_property_no = models.CharField(unique=True, max_length=50, verbose_name='dispose_equipment_property_no')
    disposed_equipment_itemname = models.CharField(max_length=50, verbose_name='dispose_equipment_itemname')
    disposed_equipment_description = models.CharField(max_length=255, verbose_name='dispose_equipment_description')
    disposed_equipment_brand = models.CharField(max_length=50, verbose_name='dispose_equipment_brand')
    disposed_equipment_model_no = models.CharField(max_length=50, verbose_name='dispose_equipment_model_no')
    disposed_equipment_serial_no = models.CharField(unique=True, max_length=50, verbose_name='dispose_equipment_serial_no')
    disposed_equipment_receiptno = models.CharField(max_length=50, verbose_name='dispose_equipment_receiptno')
    disposed_equipment_amount = models.DecimalField(max_digits=6, decimal_places=0, verbose_name='dispose_equipment_amount')
    disposed_date = models.DateTimeField(default=now, verbose_name='dispose_date')


    class Meta:
        db_table = "equipment_disposed"

class supply_email(models.Model):

    emailsupply_id = models.AutoField(primary_key=True)
    emailsupply_department = models.CharField( max_length=50, verbose_name='emailsupply_department')
    emailsupply_acceptedquantity = models.CharField( max_length=50, verbose_name='emailsupply_acceptedquantity')
    # current_date = models.CharField( max_length=50, verbose_name='currentdate')
    current_date = models.CharField(max_length=50, verbose_name='currentdate')
    current_time = models.TimeField(auto_now_add=True, blank=True, verbose_name= 'current_time')


    class Meta:
        db_table = "supply_email"

class equipment_email(models.Model):

    emailequipment_id = models.AutoField(primary_key=True)
    emailequipment_department = models.CharField(unique=True, max_length=50, verbose_name='emailequipment_department')
    emailequipment_acceptedquantity = models.CharField(unique=True, max_length=50, verbose_name='emailequipment_acceptedquantity')
    # current_date = models.CharField( max_length=50, verbose_name='currentdate')
    current_date = models.CharField(max_length=50, verbose_name='currentdate')
    current_time = models.TimeField(auto_now_add=True, blank=True, verbose_name= 'current_time')


    class Meta:
        db_table = "equipment_email"

class supply_createform(models.Model):
    createformsupply_id = models.AutoField(primary_key=True)
    createformsupply_department = models.CharField(max_length=50, verbose_name='createformsupply_department')
    createformsupply_description = models.TextField(verbose_name='createformsupply_description')
    createformsupply_unit = models.CharField( max_length=50, verbose_name='createformsupply_unit')
    createformsupply_acceptedquantity = models.CharField( max_length=50, verbose_name='createformsupply_acceptedquantity')
    createformsupply_amount = models.CharField(max_length=50, verbose_name='createformsupply_amount')
    # current_date = models.DateTimeField(default=now, verbose_name= 'createformsupply_current_date')
    current_date = models.CharField( max_length=50, verbose_name='currentdate')


    class Meta:
        db_table = "supply_createform"

class supply_createform_inputs(models.Model):
    createformsupply_inputs_id = models.AutoField(primary_key=True)
    createformsupply_inputs_office = models.CharField(max_length=255, verbose_name='createformsupply_inputs_office')
    createformsupply_inputs_department = models.CharField(unique=True, max_length=50, verbose_name='createformsupply_inputs_department')
    createformsupply_inputs_approvedby = models.CharField(max_length=50, verbose_name='createformsupply_inputs_approvedby')
    createformsupply_inputs_designation = models.CharField(max_length=50, verbose_name='createformsupply_inputs_designation')
    createformsupply_inputs_issuedby = models.CharField(max_length=50, verbose_name='createformsupply_inputs_issuedby')
    createformsupply_inputs_requestedby = models.CharField(max_length=50, verbose_name='createformsupply_inputs_requestedby')
    createformsupply_inputs_reqdesignation = models.CharField(max_length=50, verbose_name='createformsupply_inputs_reqdesignation')
    createformsupply_inputs_receivedby = models.CharField(max_length=50, verbose_name='createformsupply_inputs_receivedby')
    createformsupply_inputs_purpose = models.CharField(max_length=255, verbose_name='createformsupply_inputs_purpose')
    current_date = models.CharField( max_length=50, verbose_name='currentdate')

    class Meta:
        db_table = "supply_createform_inputs"

class equipment_createform(models.Model):

    createformequipment_id = models.AutoField(primary_key=True)
    createformequipment_department = models.CharField(unique=True, max_length=50, verbose_name='createformequipment_department')
    createformequipment_itemname = models.CharField(unique=True, max_length=50, verbose_name='createformequipment_itemname')
    createformequipment_description = models.TextField(verbose_name='createformequipment_description')
    createformequipment_brand = models.CharField(unique=True, max_length=50, verbose_name='createformequipment_brand')
    createformequipment_acceptedquantity = models.CharField(unique=True, max_length=50, verbose_name='createformequipment_acceptedquantity')
    # current_date = models.CharField( max_length=50, verbose_name='currentdate')
    current_date = models.CharField( max_length=50, verbose_name='currentdate')



    class Meta:
        db_table = "equipment_createform"


class custodian_slip(models.Model):
    custodianslip_id = models.AutoField(primary_key=True)
    custodianslip_quantity = models.DecimalField(null= True, max_digits=6, decimal_places=0, verbose_name='custodianslip_quantity')
    custodianslip_unit = models.CharField(max_length=50, verbose_name='custodianslip_unit')
    custodianslip_department = models.CharField(max_length=50, verbose_name='custodianslip_department')
    custodianslip_itemname = models.CharField(max_length=50, verbose_name='custodianslip_itemname')
    custodianslip_unitcost = models.DecimalField(null= True, max_digits=10, decimal_places=2, verbose_name='custodianslip_unitcost')
    custodianslip_totalcost = models.DecimalField(null= True, max_digits=10, decimal_places=2, verbose_name='custodianslip_totalcost')
    custodianslip_description = models.TextField(verbose_name='custodianslip_description')
    custodianslip_inventoryitemno = models.CharField(max_length=255, verbose_name='custodianslip_inventoryitemno')
    current_date = models.CharField( max_length=50, verbose_name='currentdate')

    class Meta:
        db_table = "custodian_slip"


class receiptform_equipment(models.Model):
    receiptformequipment_id = models.AutoField(primary_key=True)
    receiptformequipment_quantity = models.DecimalField(null= True, max_digits=6, decimal_places=0, verbose_name='receiptformequipment_quantity')
    receiptformequipment_itemname = models.CharField(max_length=50, verbose_name='receiptformequipment_itemname')
    receiptformequipment_department = models.CharField(max_length=50, verbose_name='receiptformequipment_itemname')
    receiptformequipment_description = models.TextField(verbose_name='receiptformequipment_desccription')
    receiptformequipment_unit = models.CharField(max_length=50, verbose_name='receiptformequipment_unit')
    receiptformequipment_propertyno = models.CharField(null= True,max_length=255, unique=True, verbose_name='receiptformequipment_propertyno')
    receiptformequipment_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='receiptformequipment_amount')
    current_date = models.CharField( max_length=50, verbose_name='currentdate')

    class Meta:
        db_table = "receiptform_equipment"

class equipment_icsform_inputs(models.Model):
    icsform_inputs_id = models.AutoField(primary_key=True)
    icsform_inputs_department = models.CharField(max_length=50, verbose_name='icsform_inputs_department')
    icsform_inputs_icsno = models.CharField(max_length=255, verbose_name='icsform_inputs_icsno')
    icsform_inputs_suppliedby = models.CharField(max_length=255, verbose_name='icsform_inputs_suppliedby')
    icsform_inputs_pono = models.CharField(max_length=255, verbose_name='icsform_inputs_pono')
    icsform_inputs_invoiceno = models.CharField(max_length=255, verbose_name='icsform_inputs_invoiceno')
    icsform_inputs_receivedfrom = models.CharField(max_length=255, verbose_name='icsform_inputs_receivedfrom')
    icsform_inputs_receivedby = models.CharField(max_length=255, verbose_name='icsform_inputs_receivedby')
    icsform_inputs_position = models.CharField(max_length=50, verbose_name='icsform_inputs_position')
    current_date = models.CharField( max_length=50, verbose_name='currentdate')


    class Meta:
        db_table = "equipment_icsform_inputs"

class equipment_areform_inputs(models.Model):
    areform_inputs_id = models.AutoField(primary_key=True)
    areform_inputs_no = models.CharField(max_length=255, verbose_name='areform_inputs_no')
    areform_inputs_department = models.CharField( max_length=50, verbose_name='areform_inputs_department')
    areform_inputs_suppliedby = models.CharField(max_length=255, verbose_name='areform_inputs_suppliedby')
    areform_inputs_pono = models.CharField(max_length=255, verbose_name='areform_inputs_pono')
    areform_inputs_invoiceno = models.CharField(max_length=255, verbose_name='areform_inputs_invoiceno')
    areform_inputs_receivedfrom = models.CharField(max_length=255, verbose_name='areform_inputs_receivedfrom')
    areform_inputs_receivedby = models.CharField(max_length=255, verbose_name='areform_inputs_receivedby')
    areform_inputs_position = models.CharField(max_length=50, verbose_name='areform_inputs_position')
    current_date = models.CharField( max_length=50, verbose_name='currentdate')

    class Meta:
        db_table = "equipment_areform_inputs"

class equipment_are_totalamount(models.Model):
    areform_totalamount_id = models.AutoField(primary_key=True)
    areform_totalamount_department = models.CharField( max_length=50, verbose_name='areform_totalamount_department')
    areform_totalamount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='areform_totalamount')
    current_date = models.CharField( max_length=50, verbose_name='currentdate')
    
    class Meta:
        db_table = "equipment_are_totalalmount"