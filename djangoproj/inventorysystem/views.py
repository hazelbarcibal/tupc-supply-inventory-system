from django.shortcuts import render, redirect
from .forms import deliverysupply, deliveryequipment
from .forms import deliverySupplyForm, deliveryEquipmentForm
from django.contrib import messages


def home(request):
    return render(request, 'task/home.html')

def adminLogin(request):
    return render(request, 'task/login.html')

def deptRegister(request):
    return render(request, 'task/department-register.html')

def suppliesDeliver(request):
    info = deliverysupply.objects.all()
    form = deliverySupplyForm()
    if request.method == 'POST':
        form = deliverySupplyForm(request.POST)
        itemname = request.POST.get('delivery_supply_itemname')
        brand = request.POST.get('delivery_supply_brand')
        if form.is_valid():
            form.save()
            messages.success(request, 'Record created for ' + brand + ' ' + itemname)
            return redirect('inventorysystem-suppliesDeliver')
    
    context = {
        'form': form,
        'info': info,
    }

    return render(request, 'task/supplies-delivery.html', context)

def addItem(request):
    return render(request, 'task/add-new-item.html')

def equipmentDeliver(request):
    info = deliveryequipment.objects.all()
    form = deliveryEquipmentForm()
    if request.method == 'POST':
        form = deliveryEquipmentForm(request.POST)
        itemname = request.POST.get('delivery_equipment_itemname')
        brand = request.POST.get('delivery_equipment_brand')
        if form.is_valid():
            form.save()
            messages.success(request, 'Record created for ' + brand + ' ' + itemname)
            return redirect('inventorysystem-equipmentDeliver')
    
    context = {
        'form': form,
        'info': info,
    }
    return render(request, 'task/equipment-delivery.html', context)

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
