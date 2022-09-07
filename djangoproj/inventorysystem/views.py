
from .models import *

from django.shortcuts import render


def home(request):
    return render(request, 'task/home.html')

def adminLogin(request):
    return render(request, 'task/login.html')

def deptRegister(request):
    return render(request, 'task/department-register.html')

def suppliesDeliver(request):
    if request.method == "POST":
        if request.POST.get('supply_delivery_itemname') and request.POST.get('supply_delivery_unit') and request.POST.get('supply_delivery_quantity'):
            update_delivery_record = deliverysupply()
            update_delivery_record.delivery_supply_itemname = request.POST.get('supply_delivery_item_name')
            update_delivery_record.delivery_supply_description = request.POST.get('supply_delivery_description')
            update_delivery_record.delivery_supply_unit = request.POST.get('supply_delivery_unit')
            update_delivery_record.delivery_supply_quantity= request.POST.get('supply_delivery_quantity')
            update_delivery_record.delivery_supply_brand = request.POST.get('supply_delivery_brand')
            update_delivery_record.save()
        else:
            return render(request, 'task/supplies-delivery.html')

    return render(request, 'task/supplies-delivery.html')

def addItem(request):
    return render(request, 'task/add-new-item.html')

def equipmentDeliver(request):
    return render(request, 'task/equipment-delivery.html')

#def addEquipment(request):
    return render(request, 'task/add-equipment.html')

def suppliesWithdraw(request):
    return render(request, 'task/supplies-withdraw.html')

def equipmentWithdraw(request):
    return render(request, 'task/equipment-withdraw.html')

def viewRequestSupply(request):
    return render(request, 'task/view-request-supplies.html')

def viewRequestEquipment(request):
    return render(request, 'task/view-request-equipment.html')

def depRequestSupply(request):
    return render(request, 'task/dep-request-supply.html')

def depRequestEquipment(request):
    return render(request, 'task/dep-request-equipment.html')

def statusLimit(request):
    return render(request, 'task/status-limit.html')

def equipmentReturn(request):
    return render(request, 'task/equipment-return.html')

def storageMapping(request):
    return render(request, 'task/storage-mapping.html')
