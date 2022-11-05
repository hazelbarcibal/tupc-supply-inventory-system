from django import forms
from .models import *
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class DeptRegisterForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(required=True, widget=forms.TextInput(attrs={'type': 'password', 'placeholder': 'Password', 'id': 'regpass'}))
    password2 = forms.CharField(required=True, widget=forms.TextInput(attrs={'type': 'password', 'placeholder': 'Retype Password', 'id': 'regpass'}))
    department = forms.CharField(required=True, widget=forms.TextInput(attrs={'list': 'department', 'placeholder': 'Department', 'pattern': '^[A-Z]+(?:_[A-Z]+)*$', 'autocomplete': 'on'}))
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'department', 'password1', 'password2']

#-------------- DELIVERY SUPPLIES ---------------
class deliverySupplyForm(forms.ModelForm):
    delivery_supply_description = forms.CharField(required=True, widget=forms.TextInput(
            attrs={'id': 'deliveryItemname', 'list': 'deliveryItemname', 'class': 'form-control', 'placeholder': 'Description'}))

    delivery_supply_unit = forms.CharField(required=True, widget=forms.TextInput(
            attrs={'list': 'deliveryUnit', 'class': 'form-control', 'placeholder': 'Unit', 'autocomplete': 'on'}))

    delivery_supply_quantity = forms.DecimalField(required=True,  widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Quantity',}))   

    delivery_supply_remaining = forms.DecimalField(required=True,  widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Remaining',}))   

    class Meta:
        model = deliverysupply
        fields = [ 'delivery_supply_description',  'delivery_supply_unit', 'delivery_supply_quantity', 'delivery_supply_remaining']

class updateDeliverySupplyForm(forms.ModelForm):
    supplymainstorage_description = forms.CharField(required=True, widget=forms.TextInput(
            attrs={'id': 'deliveryItemname', 'class': 'form-control', 'placeholder': 'Description',}))

    supplymainstorage_unit = forms.CharField(required=True, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Unit',}))


    supplymainstorage_quantity = forms.DecimalField(required=True, widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Quantity',}))  

    supplymainstorage_RequestQuantity = forms.DecimalField(required=True, widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Quantity',}))  

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
limit_quantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}))
limit_department = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}))
limit_addquantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Add Quantity'}))

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
limit_quantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}))
limit_addquantity= forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Add Quantity'}))
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
request_supply_quantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}))
request_supply_remaining= forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Remaining'}))
request_supply_mainstoragequantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mainstorage Quantity'}))
request_supply_acceptquantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Accept Quantity'}))
current_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Date & Time'}))
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
            self.fields['current_date'].widget.attrs['readonly'] = True


    class Meta:
        model = requestsupply
        fields = ['request_supply_department', 'request_supply_description', 'request_supply_unit', 'request_supply_quantity', 'request_supply_remaining',
        'current_date', 'request_supply_status', 'request_supply_mainstoragequantity', 'request_supply_acceptquantity']

#---------- withdraw supply - admin view ------------
arequest_supply_department = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}))
arequest_supply_description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}))
arequest_supply_unit = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unit'}))
arequest_supply_quantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}))
arequest_supply_remaining = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Remaining'}))
current_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Date & Time'}))
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
            self.fields['current_date'].widget.attrs['readonly'] = True

    class Meta:
        model = acceptSupplyRequests
        fields = ['arequest_supply_department', 'arequest_supply_description', 'arequest_supply_unit', 'arequest_supply_quantity', 'arequest_supply_remaining',
        'current_date', 'arequest_supply_status']


#-------------- DELIVERY EQUIPMENT ---------------
class deliveryEquipmentForm(forms.ModelForm):
    delivery_equipment_itemname = forms.CharField(required=True, widget=forms.TextInput(
            attrs={'list': 'deliveryItemname', 'id': 'itemVal', 'class': 'form-control', 'placeholder': 'Itemname'}))

    delivery_equipment_description = forms.CharField(required=True, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Description'}))

    delivery_equipment_brand = forms.CharField(required=True, widget=forms.TextInput(
            attrs={'list': 'deliveryBrand', 'class': 'form-control', 'placeholder': 'Brand'}))

    delivery_equipment_quantity = forms.DecimalField(required=True, widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Quantity'}))

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
            attrs={'class': 'form-control', 'placeholder': 'Quantity',}))  

    equipmentmainstorage_remaining= forms.DecimalField(required=True, widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Remaining',})) 

    equipmentmainstorage_RequestQuantity = forms.DecimalField(required=True, widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Request Quantity',}))  

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
request_equipment_quantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}))
request_equipment_department = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}))
request_equipment_status = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Status'}))
request_equipment_mainstoragequantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}))
request_equipment_acceptquantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}))
current_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Date and Time'}))

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
            self.fields['current_date'].widget.attrs['readonly'] = True


    class Meta:
        model = requestequipment
        fields = ['request_equipment_itemname', 'request_equipment_description', 'request_equipment_brand', 
                    'request_equipment_quantity', 'request_equipment_department', 'request_equipment_status', 
                    'request_equipment_mainstoragequantity','request_equipment_acceptquantity', 'current_date']

# dep request equipment - dep view
ItemName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item name'}))
Description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}))
Brand = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brand'}))
Quantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}))
Remaining = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Remaining'}))
RequestQuantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'RequestQuantity'}))

class depRequestEquipmentForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(depRequestEquipmentForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['ItemName'].widget.attrs['readonly'] = True
            self.fields['Description'].widget.attrs['readonly'] = True
            self.fields['Brand'].widget.attrs['readonly'] = True
            self.fields['Quantity'].widget.attrs['readonly'] = True
            self.fields['Remaining'].widget.attrs['readonly'] = True


    class Meta:
        model = equipmentmainstorage
        fields = ['ItemName', 'Description', 'Brand', 
                    'Quantity', 'Remaining', 'RequestQuantity']


# withdraw equipment - admin view
class withdrawEquipmentForm(forms.ModelForm):
    arequest_equipment_property_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Property No', 'min': '0', 'id': 'propertyNo'}))
    arequest_equipment_itemname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item Name', 'id': 'itemname'}))
    arequest_equipment_description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description', 'id': 'description'}))
    arequest_equipment_brand = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brand', 'id': 'brand'}))
    arequest_equipment_quantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity', 'min': '0', 'id': 'quantity'}))
    arequest_equipment_remaining = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Remaning', 'min': '0', 'id': 'remaining'}))
    arequest_equipment_status = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Status', 'id': 'status'}))
    arequest_equipment_yearacquired = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Year Acquired', 'id': 'yrAcquired'}))
    arequest_equipment_issued_to  = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Issued to', 'list': 'department', 'pattern': '^[A-Z]+(?:_[A-Z]+)*$', 'autocomplete': 'off', 'id': 'issuedTo'}))
    arequest_equipment_model_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Model No', 'min': '0', 'id': 'modelNo'}))
    arequest_equipment_serial_no  = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Serial No', 'min': '0', 'id': 'serialNo'}))
    arequest_equipment_certifiedcorrect = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Certified Correct', 'id': 'certified'}))
    current_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Date and Time', 'id': 'datetime'}))    
    
    def __init__(self, *args, **kwargs):
        super(withdrawEquipmentForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['arequest_equipment_department'].widget.attrs['readonly'] = True
            self.fields['arequest_equipment_itemname'].widget.attrs['readonly'] = True
            self.fields['arequest_equipment_description'].widget.attrs['readonly'] = True
            self.fields['arequest_equipment_brand'].widget.attrs['readonly'] = True
            self.fields['arequest_equipment_quantity'].widget.attrs['readonly'] = True
            self.fields['arequest_equipment_remaining'].widget.attrs['readonly'] = True
            self.fields['arequest_equipment_status'].widget.attrs['readonly'] = True
            self.fields['current_date'].widget.attrs['readonly'] = True


    class Meta:
        model = acceptEquipmentRequests
        fields = ['arequest_equipment_department', 'arequest_equipment_itemname', 'arequest_equipment_description', 
                    'arequest_equipment_brand', 'arequest_equipment_quantity', 'arequest_equipment_remaining', 
                    'arequest_equipment_status', 'arequest_equipment_yearacquired', 'arequest_equipment_issued_to',
                    'arequest_equipment_model_no', 'arequest_equipment_serial_no', 'arequest_equipment_certifiedcorrect', 'current_date' ]

# updatestorage - admin window - storagemapping models
Category = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category'}))
ItemName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ItemName'}))
RackNo = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rack'}))
LayerNo= forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'LayerNo'}))
CabinetNo = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'CabinetNo'}))
ShelfNo = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ShelfNo'}))



class storageForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(storageForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['Category'].widget.attrs['readonly'] = True
            self.fields['ItemName'].widget.attrs['readonly'] = True


    class Meta:
        model = storagemapping
        fields = ['Category', 'ItemName', 'RackNo', 'CabinetNo', 'ShelfNo', 'LayerNo']
