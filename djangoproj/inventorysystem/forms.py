from django import forms
from .models import *
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UploadFileForm(forms.Form):
        file = forms.FileField()


class DeptRegisterForm(UserCreationForm): 
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Username', 'name': 'username'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(required=True, widget=forms.TextInput(attrs={'type': 'password', 'placeholder': 'Password', 'id': 'regpass'}))
    password2 = forms.CharField(required=True, widget=forms.TextInput(attrs={'type': 'password', 'placeholder': 'Retype Password', 'id': 'regpass'}))
    department = forms.CharField(required=False, widget=forms.TextInput(attrs={'list': 'department', 'placeholder': 'Department', 'pattern': '^[A-Z]+(?:_[A-Z]+)*$', 'autocomplete': 'on'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'department', 'is_department']


class AdminRegisterForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(required=True, widget=forms.TextInput(attrs={'type': 'password', 'placeholder': 'Password', 'id': 'regpass'}))
    password2 = forms.CharField(required=True, widget=forms.TextInput(attrs={'type': 'password', 'placeholder': 'Retype Password', 'id': 'regpass'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2',  'is_staff', 'is_admin']

        
class AdminUpdateForm(forms.ModelForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'email']

class DeptUpdateForm(forms.ModelForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'email']
        

#-------------- DELIVERY SUPPLIES ---------------
class deliverySupplyForm(forms.ModelForm):
        delivery_supply_description = forms.CharField(required=True, widget=forms.TextInput(
                attrs={'list': 'deliveryItemname', 'class': 'form-control', 'placeholder': 'Description', 'autocomplete': 'on', 'id': 'delivery_supply_description'}))

        delivery_supply_unit = forms.CharField(required=True, widget=forms.TextInput(
                attrs={'list': 'deliveryUnit', 'class': 'form-control', 'placeholder': 'Unit', 'autocomplete': 'on', 'id': 'delivery_supply_unit'}))

        delivery_supply_quantity = forms.DecimalField(required=True,  widget=forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Quantity', 'min': 1, 'id': 'delivery_supply_quantity'}))   

        delivery_supply_remaining = forms.DecimalField(required=True,  widget=forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Remaining', 'id': 'delivery_supply_remaining'}))   

        delivery_supplyRackNo = forms.DecimalField(required=True,  widget=forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Rack No.', 'min': 0, 'id': 'delivery_supplyRackNo'}))   

        delivery_supplyLayerNo = forms.DecimalField(required=True,  widget=forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Layer No.', 'min': 0, 'id': 'delivery_supplyLayerNo'})) 

        delivery_supplyCabinetNo = forms.DecimalField(required=True,  widget=forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Cabinet No.', 'min': 0, 'id': 'delivery_supplyCabinetNo'})) 

        delivery_supplyShelfNo = forms.DecimalField(required=True,  widget=forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Shelf No.', 'min': 0, 'id': 'delivery_supplyShelfNo'})) 

        class Meta:
                model = deliverysupply
                fields = [ 'delivery_supply_description',  'delivery_supply_unit', 'delivery_supply_quantity', 'delivery_supply_remaining', 'delivery_supplyRackNo',
                                'delivery_supplyLayerNo', 'delivery_supplyCabinetNo', 'delivery_supplyShelfNo']


class updateDeliverySupplyForm(forms.ModelForm):
    supplymainstorage_description = forms.CharField(required=True, widget=forms.TextInput(
            attrs={'id': 'deliveryItemname', 'class': 'form-control', 'placeholder': 'Description',}))

    supplymainstorage_unit = forms.CharField(required=True, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Unit',}))


    supplymainstorage_quantity = forms.DecimalField(required=True, widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Quantity',}))  

    supplymainstorage_RequestQuantity = forms.DecimalField(required=True, widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Quantity', 'min': 1,}))  

    def __init__(self, *args, **kwargs):
        super(updateDeliverySupplyForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['supplymainstorage_description'].widget.attrs['readonly'] = True
            self.fields['supplymainstorage_unit'].widget.attrs['readonly'] = True
            self.fields['supplymainstorage_quantity'].widget.attrs['readonly'] = True

    class Meta:
        model = supplymainstorage
        fields = ['supplymainstorage_description', 'supplymainstorage_unit', 'supplymainstorage_quantity', 'supplymainstorage_RequestQuantity']

# updatestatuslimit - admin window - limitrecord models
limit_description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}))
limit_unit = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unit'}))
limit_quantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity', 'min': 1,}))
limit_department = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}))
limit_addquantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Add Quantity', 'min': 1,}))

class statusForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(statusForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:           
            self.fields['limit_description'].widget.attrs['readonly'] = True
            self.fields['limit_unit'].widget.attrs['readonly'] = True
            self.fields['limit_quantity'].widget.attrs['readonly'] = True
            self.fields['limit_department'].widget.attrs['readonly'] = True


    class Meta:
        model = limitrecords
        fields = ['limit_description', 'limit_unit', 'limit_quantity', 'limit_department', 'limit_addquantity']



# supply request - admin window - mainstorage models
limit_description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}))
limit_unit = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unit'}))
limit_quantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity', 'min': 1,}))
limit_addquantity= forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Add Quantity', 'min': 1,}))
class depRequestSupplyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(depRequestSupplyForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:           
            self.fields['limit_description'].widget.attrs['readonly'] = True
            self.fields['limit_unit'].widget.attrs['readonly'] = True
            self.fields['limit_quantity'].widget.attrs['readonly'] = True


    class Meta:
        model = limitrecords
        fields = ['limit_description', 'limit_unit','limit_quantity', 'limit_addquantity']

#------ Request supply - admin window ------------
request_supply_department = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}))
request_supply_description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}))
request_supply_unit = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unit'}))
request_supply_quantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity', 'min': 1,}))
request_supply_remaining= forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Remaining'}))
request_supply_mainstoragequantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mainstorage Quantity', 'min': 1,}))
request_supply_acceptquantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Accept Quantity', 'min': 1,}))
request_supply_daterequested = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date Requested'}))
request_supply_status = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Status'}))

class requestSupplyForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(requestSupplyForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['request_supply_department'].widget.attrs['readonly'] = True
            self.fields['request_supply_description'].widget.attrs['readonly'] = True
            self.fields['request_supply_unit'].widget.attrs['readonly'] = True
            self.fields['request_supply_quantity'].widget.attrs['readonly'] = True
            self.fields['request_supply_remaining'].widget.attrs['readonly'] = True
            self.fields['request_supply_mainstoragequantity'].widget.attrs['readonly'] = True
            self.fields['request_supply_daterequested'].widget.attrs['readonly'] = True


    class Meta:
        model = requestsupply
        fields = ['request_supply_department', 'request_supply_description', 'request_supply_unit', 'request_supply_quantity', 'request_supply_remaining',
         'request_supply_status', 'request_supply_mainstoragequantity', 'request_supply_acceptquantity', 'request_supply_daterequested']

#---------- withdraw supply - admin view ------------
arequest_supply_department = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}))
arequest_supply_description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}))
arequest_supply_unit = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unit'}))
arequest_supply_quantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity', 'min': 1,}))
arequest_supply_remaining = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Remaining'}))
arequest_supply_daterequested = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date'}))
arequest_supply_dateaccepted = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date'}))
arequest_supply_status = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Status'}))

class withdrawStatusForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(withdrawStatusForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['arequest_supply_department'].widget.attrs['readonly'] = True
            self.fields['arequest_supply_description'].widget.attrs['readonly'] = True
            self.fields['arequest_supply_unit'].widget.attrs['readonly'] = True
            self.fields['arequest_supply_quantity'].widget.attrs['readonly'] = True
            self.fields['arequest_supply_remaining'].widget.attrs['readonly'] = True
            self.fields['arequest_supply_daterequested'].widget.attrs['readonly'] = True
            self.fields['arequest_supply_dateaccepted'].widget.attrs['readonly'] = True

    class Meta:
        model = acceptSupplyRequests
        fields = ['arequest_supply_department', 'arequest_supply_description', 'arequest_supply_unit', 'arequest_supply_quantity', 'arequest_supply_remaining',
        'arequest_supply_daterequested', 'arequest_supply_dateaccepted','arequest_supply_status']


#-------------- DELIVERY EQUIPMENT ---------------
class deliveryEquipmentForm(forms.ModelForm):
    delivery_equipment_itemname = forms.CharField(required=True, widget=forms.TextInput(
            attrs={'list': 'deliveryItemname', 'id': 'itemVal', 'class': 'form-control', 'placeholder': 'Itemname'}))

    delivery_equipment_description = forms.CharField(required=True, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Description'}))

    delivery_equipment_brand = forms.CharField(required=True, widget=forms.TextInput(
            attrs={'list': 'deliveryBrand', 'class': 'form-control', 'placeholder': 'Brand'}))

    delivery_equipment_quantity = forms.DecimalField(required=True, widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Quantity', 'min': 1,}))

    class Meta:
        model = deliveryequipment
        fields = ['delivery_equipment_itemname', 'delivery_equipment_description', 'delivery_equipment_brand', 'delivery_equipment_quantity']

class updateEquipmentSupplyForm(forms.ModelForm):
    equipmentmainstorage_itemName = forms.CharField(required=True, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Itemname',}))

    equipmentmainstorage_description = forms.CharField(required=True, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Unit', 'autocomplete': 'on'}))

    equipmentmainstorage_brand = forms.CharField(required=True, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Brand',}))


    equipmentmainstorage_quantity = forms.DecimalField(required=True, widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Quantity', 'min': 1,}))  

    equipmentmainstorage_remaining= forms.DecimalField(required=True, widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Remaining',})) 

    equipmentmainstorage_RequestQuantity = forms.DecimalField(required=True, widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Add Quantity', 'min': 1,}))  

    def __init__(self, *args, **kwargs):
        super(updateEquipmentSupplyForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['equipmentmainstorage_itemName'].widget.attrs['readonly'] = True
            self.fields['equipmentmainstorage_description'].widget.attrs['readonly'] = True
            self.fields['equipmentmainstorage_brand'].widget.attrs['readonly'] = True
            self.fields['equipmentmainstorage_quantity'].widget.attrs['readonly'] = True

    class Meta:
        model = equipmentmainstorage
        fields = ['equipmentmainstorage_itemName', 'equipmentmainstorage_description', 'equipmentmainstorage_brand', 
        'equipmentmainstorage_quantity', 'equipmentmainstorage_remaining', 'equipmentmainstorage_RequestQuantity']


# request equipment - admin view
request_equipment_itemname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item name'}))
request_equipment_description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}))
request_equipment_brand = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brand'}))
request_equipment_quantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity', 'min': 1,}))
request_equipment_department = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}))
request_equipment_status = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Status'}))
request_equipment_mainstoragequantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity', 'min': 1,}))
request_equipment_acceptquantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity', 'min': 1,}))
request_equipment_daterequested = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date Requested'}))

class equipmentRequestForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(equipmentRequestForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['request_equipment_itemname'].widget.attrs['readonly'] = True
            self.fields['request_equipment_description'].widget.attrs['readonly'] = True
            self.fields['request_equipment_brand'].widget.attrs['readonly'] = True
            self.fields['request_equipment_quantity'].widget.attrs['readonly'] = True
            self.fields['request_equipment_mainstoragequantity'].widget.attrs['readonly'] = True
            self.fields['request_equipment_department'].widget.attrs['readonly'] = True
            self.fields['request_equipment_daterequested'].widget.attrs['readonly'] = True


    class Meta:
        model = requestequipment
        fields = ['request_equipment_itemname', 'request_equipment_description', 'request_equipment_brand', 
                    'request_equipment_quantity', 'request_equipment_department', 'request_equipment_status', 
                    'request_equipment_mainstoragequantity','request_equipment_acceptquantity', 'request_equipment_daterequested']

# dep request equipment - dep view
equipmentmainstorage_itemName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item name'}))
equipmentmainstorage_description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}))
equipmentmainstorage_brand = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brand'}))
equipmentmainstorage_quantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity', 'min': 1,}))
equipmentmainstorage_remaining = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Remaining'}))
equipmentmainstorage_RequestQuantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'RequestQuantity'}))

class depRequestEquipmentForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(depRequestEquipmentForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['equipmentmainstorage_itemName'].widget.attrs['readonly'] = True
            self.fields['equipmentmainstorage_description'].widget.attrs['readonly'] = True
            self.fields['equipmentmainstorage_brand'].widget.attrs['readonly'] = True
            self.fields['equipmentmainstorage_quantity'].widget.attrs['readonly'] = True
            self.fields['equipmentmainstorage_remaining'].widget.attrs['readonly'] = True


    class Meta:
        model = equipmentmainstorage
        fields = ['equipmentmainstorage_itemName', 'equipmentmainstorage_description', 'equipmentmainstorage_brand', 
                    'equipmentmainstorage_quantity', 'equipmentmainstorage_remaining', 'equipmentmainstorage_RequestQuantity']



# withdraw equipment - admin view
class withdrawEquipmentForm(forms.ModelForm):
    arequest_equipment_property_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Property No', 'min': '0', 'id': 'propertyNo'}))
    arequest_equipment_itemname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item Name', 'id': 'itemname'}))
    arequest_equipment_description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description', 'id': 'description'}))
    arequest_equipment_brand = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brand', 'id': 'brand'}))
    arequest_equipment_quantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity', 'min': '1', 'id': 'quantity'}))
    arequest_equipment_remaining = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Remaning', 'min': '1', 'id': 'remaining'}))
    arequest_equipment_status = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Status', 'id': 'status'}))
    arequest_equipment_yearacquired = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Year Acquired', 'id': 'yrAcquired'}))
    arequest_equipment_issued_to  = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Issued to', 'list': 'department', 'pattern': '^[A-Z]+(?:_[A-Z]+)*$', 'autocomplete': 'off', 'id': 'issuedTo'}))
    arequest_equipment_model_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Model No', 'min': '1', 'id': 'modelNo'}))
    arequest_equipment_serial_no  = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Serial No', 'min': '1', 'id': 'serialNo'}))
    arequest_equipment_certifiedcorrect = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Certified Correct', 'id': 'certified'}))
    arequest_equipment_daterequested = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Status', 'id': 'DateRequested'}))   
    arequest_equipment_dateaccepted = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date Accepted', 'id': 'DateAccepted'}))

    def __init__(self, *args, **kwargs):
        super(withdrawEquipmentForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['arequest_equipment_issued_to'].widget.attrs['readonly'] = True
            self.fields['arequest_equipment_itemname'].widget.attrs['readonly'] = True
            self.fields['arequest_equipment_description'].widget.attrs['readonly'] = True
            self.fields['arequest_equipment_brand'].widget.attrs['readonly'] = True
            self.fields['arequest_equipment_quantity'].widget.attrs['readonly'] = True
            self.fields['arequest_equipment_remaining'].widget.attrs['readonly'] = True
            self.fields['arequest_equipment_daterequested'].widget.attrs['readonly'] = True
            self.fields['arequest_equipment_dateaccepted'].widget.attrs['readonly'] = True


    class Meta:
        model = acceptEquipmentRequests
        fields = ['arequest_equipment_issued_to', 'arequest_equipment_itemname', 'arequest_equipment_description', 
                    'arequest_equipment_brand', 'arequest_equipment_quantity', 'arequest_equipment_remaining', 
                    'arequest_equipment_status', 'arequest_equipment_yearacquired',
                    'arequest_equipment_model_no', 'arequest_equipment_serial_no', 'arequest_equipment_certifiedcorrect', 'arequest_equipment_daterequested', 'arequest_equipment_dateaccepted']

# update-supply-storage - admin window - storagemapping models
supplyItemName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ItemName'}))
supplyRackNo = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rack', 'min': 1,}))
supplyLayerNo= forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'LayerNo', 'min': 1,}))
supplyCabinetNo = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'CabinetNo', 'min': 1,}))
supplyShelfNo = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ShelfNo', 'min': 1,}))



class supply_storageForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(supply_storageForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['supplyItemName'].widget.attrs['readonly'] = True


    class Meta:
        model = supply_storagemapping
        fields = ['supplyItemName', 'supplyRackNo', 'supplyCabinetNo', 'supplyShelfNo', 'supplyLayerNo']

# update-equipment-storage - admin window - storagemapping models
equipmentItemName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ItemName'}))
equipmentLocation = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Location', 'min': 1,}))


# supply_createform - admin view
class supplycreateforminputsForm(forms.ModelForm):
        createformsupply_inputs_office = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Office', 'id': 'createformsupply_inputs_office'}))
        createformsupply_inputs_requestedby = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Requested by', 'id': 'createformsupply_inputs_requestedby'}))
        createformsupply_inputs_purpose = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Purpose', 'id': 'createformsupply_inputs_purpose'}))
        createformsupply_inputs_approvedby = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Approved by', 'id': 'createformsupply_inputs_approvedby'}))
        createformsupply_inputs_issuedby = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Issued By', 'id': 'createformsupply_inputs_issuedby'}))
        createformsupply_inputs_receivedby = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Received by', 'id': 'createformsupply_inputs_receivedby'}))
        current_date = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True, 'id': 'date'}))

        class Meta:
                model = supply_createform_inputs
                fields = ['createformsupply_inputs_office', 'createformsupply_inputs_requestedby', 
                        'createformsupply_inputs_purpose', 'createformsupply_inputs_approvedby', 'createformsupply_inputs_issuedby', 'createformsupply_inputs_receivedby', 'current_date' ]

class equipment_icsform_inputsForm(forms.ModelForm):
        icsform_inputs_department = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True, 'id': 'department'}))
        icsform_inputs_icsno = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ICS No', 'id': 'icsform_inputs_icsno'}))
        icsform_inputs_suppliedby = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Supplied By', 'id': 'icsform_inputs_suppliedby'}))
        icsform_inputs_pono = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PO No', 'id': 'icsform_inputs_pono'}))
        icsform_inputs_invoiceno = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Invoice No.', 'id': 'icsform_inputs_invoiceno'}))
        icsform_inputs_receivedfrom = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Received form', 'id': 'icsform_inputs_receivedfrom'}))
        icsform_inputs_receivedby = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Received by', 'id': 'icsform_inputs_receivedby'}))
        current_date = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True, 'id': 'date'}))

        class Meta:
                model = equipment_icsform_inputs
                fields = ['icsform_inputs_icsno', 'icsform_inputs_suppliedby', 
                        'icsform_inputs_pono', 'icsform_inputs_invoiceno', 'icsform_inputs_receivedfrom' , 'icsform_inputs_receivedby', 'icsform_inputs_department', 'current_date']

class equipment_areform_inputsForm(forms.ModelForm):
        areform_inputs_no = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ICS No', 'id': 'areform_inputs_no'}))
        areform_inputs_suppliedby = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Supplied by', 'id': 'areform_inputs_suppliedby'}))
        areform_inputs_pono = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PO No', 'id': 'areform_inputs_pono'}))
        areform_inputs_invoiceno = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Invoice No.', 'id': 'areform_inputs_invoiceno'}))
        areform_inputs_receivedfrom = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Received from', 'id': 'areform_inputs_receivedfrom'}))
        areform_inputs_receivedby = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Received by', 'id': 'areform_inputs_receivedby'}))
        areform_inputs_totalamount = forms.DecimalField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total Amount', 'id': 'areform_inputs_totalamount'}))
        current_date = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True, 'id': 'date'}))
        areform_inputs_department = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True, 'id': 'department'}))

        class Meta:
                model = equipment_areform_inputs
                fields = ['areform_inputs_no', 'areform_inputs_suppliedby', 'areform_inputs_pono', 'areform_inputs_invoiceno', 
                'areform_inputs_receivedfrom', 'areform_inputs_receivedby', 'areform_inputs_totalamount', 'current_date', 'areform_inputs_department']