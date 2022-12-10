from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser  
from django.utils.timezone import now


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
    current_date = models.DateTimeField(auto_now_add=True, blank=True, verbose_name= 'delivery_current_date')

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
    request_supply_supplyRackNo = models.CharField(null= True, max_length=50, verbose_name='request_supply_Rack')
    request_supply_supplyLayerNo = models.DecimalField(null= True, max_digits=6, decimal_places=0, verbose_name='request_supply_Layer')
    request_supply_supplyCabinetNo = models.DecimalField(null= True, max_digits=6, decimal_places=0, verbose_name='request_supply_Cabinet')
    request_supply_supplyShelfNo = models.DecimalField(null= True, max_digits=6, decimal_places=0, verbose_name='request_supply_Shelf')
    current_date = models.DateTimeField(default=now, verbose_name= 'request_current_date')

    class Meta:
        db_table = ('requestsupply')

class withdrawsupply(models.Model):

    withdrawsupply_id = models.AutoField(primary_key=True)
    withdraw_supply_department = models.CharField(max_length=50, verbose_name='withdraw_supply_department')
    withdraw_supply_description = models.CharField(max_length=255, verbose_name='withdraw_supply_description')
    withdraw_supply_unit = models.CharField(max_length=50, verbose_name='withdraw_supply_unit')
    withdraw_supply_quantity = models.DecimalField(max_digits=6, decimal_places=0, verbose_name='withdraw_supply_quantity')
    withdraw_supply_remaining = models.DecimalField(null=True, max_digits=6, decimal_places=0, verbose_name='withdraw_supply_remaining')
    current_date = models.DateTimeField(default=now, verbose_name='withdraw_current_date')

    db_table = "withdrawsupply"

class limitrecords(models.Model):

    limit_id = models.AutoField(primary_key=True)
    limit_description = models.CharField(max_length=255, verbose_name='limit_description')
    limit_unit = models.CharField(max_length=50, verbose_name='limit_unit')
    limit_quantity = models.DecimalField(max_digits=6, decimal_places=0, verbose_name='limit_quantity')
    limit_department = models.CharField(max_length=50, verbose_name='limit_department')
    limit_addquantity = models.DecimalField(null=True, max_digits=6, decimal_places=0, verbose_name='limit_addquantity')
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
    current_date = models.DateTimeField(default=now, verbose_name='supplymainstorage_current_date')
    
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
    current_date = models.CharField(max_length=50, verbose_name='currentdate')

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
    current_date = models.DateTimeField(default=now, editable=False, verbose_name= 'delivery_current_date')

    class Meta:
        db_table = ('deliveryequipment')

class requestequipment(models.Model):

    requestequipment_id = models.AutoField(primary_key=True)
    request_equipment_itemname = models.CharField(max_length=50, verbose_name='request_equipment_itemname')
    request_equipment_description = models.CharField(max_length=255, verbose_name='request_equipment_description')
    request_equipment_brand = models.CharField(max_length=50, verbose_name='request_equipment_brand')
    request_equipment_quantity = models.DecimalField(max_digits=6, decimal_places=0, verbose_name='request_equipment_quantity')
    request_equipment_department = models.CharField(max_length=50, verbose_name='request_equipment_department')
    request_equipment_status = models.CharField(max_length=50, verbose_name='request_equipment_status')
    request_equipment_mainstoragequantity = models.DecimalField(null=True, max_digits=6, decimal_places=0, max_length=50, verbose_name='request_equipment_mainstoragequantity')
    request_equipment_acceptquantity = models.DecimalField(null=True, max_digits=6, decimal_places=0, max_length=50, verbose_name='request_equipment_acceptquantity')
    current_date = models.DateTimeField(default=now, verbose_name= 'request_current_date')

    class Meta:
        db_table = ('requestequipment')

class acceptEquipmentRequests(models.Model):

    acceptEquipmentRequests_id = models.AutoField(primary_key=True)
    arequest_equipment_property_no = models.CharField(null = True, max_length=50, verbose_name='arequest_equipment_property_no')
    # wag gamitin to - arequest_equipment_department = models.CharField(max_length=50, verbose_name='arequest_equipment_department')
    arequest_equipment_itemname = models.CharField(max_length=255, verbose_name='arequest_equipment_itemname')
    arequest_equipment_description = models.CharField(max_length=255, verbose_name='arequest_equipment_description')
    arequest_equipment_brand = models.CharField(max_length=50, verbose_name='arequest_equipment_brand')
    arequest_equipment_quantity = models.DecimalField(max_digits=6,decimal_places=0, verbose_name='arequest_equipment_quantity')
    arequest_equipment_remaining = models.DecimalField(null=True, max_digits=6,decimal_places=0, verbose_name='arequest_equipment_remaining')
    arequest_equipment_status = models.CharField(max_length=50, verbose_name='arequest_equipment_status')
    arequest_equipment_yearacquired = models.CharField(max_length=50, verbose_name='arequest_yearacquired')
    arequest_equipment_issued_to = models.CharField(max_length=50, verbose_name='arequest_equipment_issued_to')
    arequest_equipment_model_no = models.CharField(max_length=50, verbose_name='arequest_equipment_model_no')
    arequest_equipment_serial_no = models.CharField(null = True, max_length=50, verbose_name='arequest_equipment_serial_no')
    arequest_equipment_certifiedcorrect = models.CharField(max_length=50, verbose_name='arequest_equipment_certifiedcorrect')
    current_date = models.DateTimeField(default=now, verbose_name= 'arequest_current_date')

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
    current_date = models.DateTimeField(default=now, verbose_name='withdraw_current_date')
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

class supply_email(models.Model):

    emailsupply_id = models.AutoField(primary_key=True)
    emailsupply_department = models.CharField( max_length=50, verbose_name='emailsupply_department')
    emailsupply_acceptedquantity = models.CharField( max_length=50, verbose_name='emailsupply_acceptedquantity')
    current_date = models.CharField( max_length=50, verbose_name='currentdate')


    class Meta:
        db_table = "supply_email"

class equipment_email(models.Model):

    emailequipment_id = models.AutoField(primary_key=True)
    emailequipment_department = models.CharField(unique=True, max_length=50, verbose_name='emailequipment_department')
    emailequipment_acceptedquantity = models.CharField(unique=True, max_length=50, verbose_name='emailequipment_acceptedquantity')
    current_date = models.CharField( max_length=50, verbose_name='currentdate')


    class Meta:
        db_table = "equipment_email"