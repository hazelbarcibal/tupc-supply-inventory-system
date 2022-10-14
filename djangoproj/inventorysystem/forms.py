from django import forms
from .models import *
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class DeptRegisterForm(UserCreationForm):
    #department = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Department'}))
    #department = forms.CharField(required=True, widget=forms.TextInput(attrs={'name': 'department', 'placeholder': 'Department'}))
    

    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(required=True, widget=forms.TextInput(attrs={'type': 'password', 'placeholder': 'Password', 'id': 'regpass'}))
    password2 = forms.CharField(required=True, widget=forms.TextInput(attrs={'type': 'password', 'placeholder': 'Retype Password', 'id': 'regpass'}))
    #department = forms.ChoiceField(required=True, choices=dept_office)
    department = forms.CharField(required=True, widget=forms.TextInput(attrs={'list': 'department', 'placeholder': 'Department', 'pattern': '^[A-Z]+(?:_[A-Z]+)*$', 'autocomplete': 'off'}))
    
    class Meta:
        model = CustomUser
        fields = ['username', 'department', 'password1', 'password2']


class deliverySupplyForm(forms.ModelForm):
    delivery_supply_itemname = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'itemVal',
                'class': 'form-control'
            }
        )
    )

    delivery_supply_unit = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'unitVal',
                'class': 'form-control'
            }
        )
    )

    delivery_supply_description = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )


    delivery_supply_quantity = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control'
            }
        )
    )   


    class Meta:
        model = deliverysupply
        fields = ['delivery_supply_itemname', 'delivery_supply_unit', 'delivery_supply_description', 'delivery_supply_quantity']


class deliveryEquipmentForm(forms.ModelForm):
    delivery_equipment_itemname = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'itemVal',
                'class': 'form-control'
            }
        )
    )

    delivery_equipment_unit = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'unitVal',
                'class': 'form-control'
            }
        )
    )

    delivery_equipment_description = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    delivery_equipment_brand = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    delivery_equipment_quantity = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = deliveryequipment
        fields = ['delivery_equipment_itemname', 'delivery_equipment_unit', 'delivery_equipment_description', 'delivery_equipment_brand', 'delivery_equipment_quantity']



# Request supply - admin window
request_supply_department = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}))
request_supply_itemname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item name'}))
request_supply_description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}))
request_supply_unit = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unit'}))
request_supply_quantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}))
request_supply_remaining= forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Remaining'}))
current_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Date & Time'}))
request_supply_status = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Status'}))

class requestSupplyForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(requestSupplyForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['request_supply_department'].widget.attrs['readonly'] = True
            self.fields['request_supply_itemname'].widget.attrs['readonly'] = True
            self.fields['request_supply_description'].widget.attrs['readonly'] = True
            self.fields['request_supply_unit'].widget.attrs['readonly'] = True
            self.fields['request_supply_quantity'].widget.attrs['readonly'] = True
            self.fields['request_supply_remaining'].widget.attrs['readonly'] = True
            self.fields['current_date'].widget.attrs['readonly'] = True


    class Meta:
        model = requestsupply
        fields = ['request_supply_department', 'request_supply_itemname', 'request_supply_description', 'request_supply_unit', 'request_supply_quantity', 'request_supply_remaining',
        'current_date', 'request_supply_status']

# Accept Request supply - admin window
arequest_supply_department = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}))
arequest_supply_itemname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item name'}))
arequest_supply_description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}))
arequest_supply_unit = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unit'}))
arequest_supply_quantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}))
arequest_supply_remaining = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Remaining'}))
current_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Date & Time'}))
arequest_supply_status = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Status'}))

class acceptSupplyRequestsForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(acceptSupplyRequestsForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['request_supply_department'].widget.attrs['readonly'] = True
            self.fields['request_supply_itemname'].widget.attrs['readonly'] = True
            self.fields['request_supply_description'].widget.attrs['readonly'] = True
            self.fields['request_supply_unit'].widget.attrs['readonly'] = True
            self.fields['request_supply_quantity'].widget.attrs['readonly'] = True
            self.fields['request_supply_remaining'].widget.attrs['readonly'] = True
            self.fields['current_date'].widget.attrs['readonly'] = True

    class Meta:
        model = requestsupply
        fields = ['request_supply_department', 'request_supply_itemname', 'request_supply_description', 'request_supply_unit', 'request_supply_quantity', 'request_supply_remaining',
        'current_date', 'request_supply_status']


# withdraw supply - admin view
arequest_supply_department = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}))
arequest_supply_itemname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item name'}))
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
            self.fields['arequest_supply_itemname'].widget.attrs['readonly'] = True
            self.fields['arequest_supply_description'].widget.attrs['readonly'] = True
            self.fields['arequest_supply_unit'].widget.attrs['readonly'] = True
            self.fields['arequest_supply_quantity'].widget.attrs['readonly'] = True
            self.fields['arequest_supply_remaining'].widget.attrs['readonly'] = True
            self.fields['current_date'].widget.attrs['readonly'] = True

    class Meta:
        model = acceptSupplyRequests
        fields = ['arequest_supply_department', 'arequest_supply_itemname', 'arequest_supply_description', 'arequest_supply_unit', 'arequest_supply_quantity', 'arequest_supply_remaining',
        'current_date', 'arequest_supply_status']



# storage - admin window
Category = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category'}))
ItemName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ItemName'}))
Location = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Location'}))
CabinetNo = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'CabinetNo'}))
ShelfNo = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ShelfNo'}))
LayerNo= forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'LayerNo'}))


class storageForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(storageForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['Category'].widget.attrs['readonly'] = True
            self.fields['ItemName'].widget.attrs['readonly'] = True


    class Meta:
        model = storagemapping
        fields = ['Category', 'ItemName', 'Location', 'CabinetNo', 'ShelfNo', 'LayerNo']
