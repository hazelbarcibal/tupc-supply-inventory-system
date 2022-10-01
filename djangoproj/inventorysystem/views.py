from .forms import *
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse, HttpResponseRedirect, response
from django.contrib import messages
import datetime
import xlwt

def home(request):
    return render(request, 'task/home.html')

def userLogin(request):

    return render(request, 'task/login.html')

def deptRegister(request):
    form = DeptRegisterForm()
    
    if request.method == "POST":
        form = DeptRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('inventorysystem-deptRegister')
        else:
            messages.warning(request, form.errors)
    context = {
        'form': form,
        
    }
    return render(request, 'task/department-register.html', context)

def suppliesDeliver(request):
    info = deliverysupply.objects.all()
    form = deliverySupplyForm()
    if request.method == 'POST':
        form = deliverySupplyForm(request.POST)
        itemname = request.POST.get('delivery_supply_itemname')
        brand = request.POST.get('delivery_supply_brand')
        description = request.POST.get('delivery_supply_description')
        unit = request.POST.get('delivery_supply_unit')
        quantity = request.POST.get('delivery_supply_quantity')

        if  deliverysupply.objects.filter(delivery_supply_itemname = itemname).exists() == False:
            if form.is_valid():
                form.save()
                messages.success(request, 'Record created for ' + brand + ' ' + itemname)
                return redirect('inventorysystem-suppliesDeliver')

        elif deliverysupply.objects.filter(delivery_supply_itemname = itemname).exists() == True:
            getdata = deliverysupply.objects.get(delivery_supply_itemname = itemname)
            updating = int(getdata.delivery_supply_quantity) + int(quantity)
            form2 = deliverysupply()
            form2.delivery_supply_itemname = itemname
            form2.delivery_supply_brand = brand
            form2.delivery_supply_description = description
            form2.delivery_supply_unit = unit
            form2.delivery_supply_quantity = quantity
            form2.delivery_supply_remaining = updating
            form2.save()
            messages.success(request, 'Record updated for ' + brand + ' ' + itemname)
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
        description = request.POST.get('delivery_equipment_description')
        unit = request.POST.get('delivery_equipment_unit')
        quantity = request.POST.get('delivery_equipment_quantity')

        if deliveryequipment.objects.filter(delivery_equipment_itemname = itemname).exists() == False:
            if form.is_valid():
                form.save()
                messages.success(request, 'Record created for ' + brand + ' ' + itemname)
                return redirect('inventorysystem-equipmentDeliver')

        elif deliveryequipment.objects.filter(delivery_equipment_itemname = itemname).exists() == True:
            getdata = deliveryequipment.objects.get(delivery_equipment_itemname = itemname)
            updating = int(getdata.delivery_equipment_quantity) + int(quantity)
            form2 = deliveryequipment()
            form2.delivery_equipment_itemname = itemname
            form2.delivery_equipment_brand = brand
            form2.delivery_equipment_description = description
            form2.delivery_equipment_unit = unit
            form2.delivery_equipment_quantity = quantity
            form2.delivery_equipment_remaining = updating
            form2.save()
            messages.success(request, 'Record updated for ' + brand + ' ' + itemname)
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

def export_excel(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Supply Inventory' + \
        str(datetime.datetime.now())+'.xls'
    wb =xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Supply Delivery')
    ws1 = wb.add_sheet('Equipment Delivery')
    row_num = 0
    row_num1 = 0
    supply_font = xlwt.XFStyle()
    equipment_font = xlwt.XFStyle()
    

#supply delivery
    supply_font.font.bold = True
    supplydelivery = ['Itemname', 'Description', 'Brand', 'Unit',
                'Quantity', 'Remaining Quantity', 'Date']

    for col_num in range(len(supplydelivery)):
        ws.write(row_num,col_num, supplydelivery[col_num], supply_font)

    font_style = xlwt.XFStyle()

    rows = deliverysupply.objects.all().values_list(
        'delivery_supply_itemname', 'delivery_supply_description', 'delivery_supply_brand', 'delivery_supply_unit',
                'delivery_supply_quantity', 'delivery_supply_remaining', 'current_date')

    for row in rows:
        row_num+= 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)


#equipment delivery
    equipment_font.font.bold = True
    equipmentdelivery = ['Itemname', 'Description', 'Brand', 'Serial No.',
                'Quantity', 'Remaining Quantity', 'Date']

    for col_num1 in range(len(equipmentdelivery)):
        ws1.write(row_num1,col_num1, equipmentdelivery[col_num1], equipment_font)

    font_style = xlwt.XFStyle()

    rows1 =deliveryequipment.objects.all().values_list(
        'delivery_equipment_itemname', 'delivery_equipment_description', 'delivery_equipment_brand', 'delivery_equipment_unit',
                'delivery_equipment_quantity', 'delivery_equipment_remaining', 'current_date')

    for row in rows1:
        row_num1+= 1

        for col_num1 in range(len(row)):
            ws1.write(row_num1, col_num1, str(row[col_num1]), font_style)

    wb.save(response)
    return response
