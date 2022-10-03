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

    delivery_supply_brand = forms.CharField(
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
        fields = ['delivery_supply_itemname', 'delivery_supply_unit', 'delivery_supply_description', 'delivery_supply_brand', 'delivery_supply_quantity']


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