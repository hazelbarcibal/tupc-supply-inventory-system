from .forms import *
from .models import *
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse, HttpResponseRedirect, response
from django.contrib import messages
import datetime
import xlwt

def home(request):
    return render(request, 'task/home.html')

def deptLogin(request):
    if request.method == "POST":
        deptuser = request.POST.get('logusername')
        department1 = request.POST.get('logdept')
        deptpass = request.POST.get('logpassword')
        user = authenticate(request, department=department1, username=deptuser,  password=deptpass)

        if user is not None and user.is_active and user.is_department:
            login(request, user)
            messages.success(request, 'Hello ' + deptuser + '!')
            return redirect('inventorysystem-depRequestSupply')
        else:
            messages.info(request, 'Invalid credentials. Please try again.')
    return render(request, 'task/department-login.html')

def userLogin(request):
    if request.method == "POST":
        adminuser = request.POST.get('logname')
        adminpass = request.POST.get('logpass')
        user = authenticate(request, username=adminuser, password=adminpass)

        if user is not None and user.is_superuser:
            login(request, user)
            messages.success(request, 'Hello ' + adminuser + '!')
            return redirect('inventorysystem-home')
        else:
            messages.info(request, 'Invalid credentials. Please try again.')

    return render(request, 'task/admin-login.html')


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
    info1 = supplymainstorage.objects.all()
    form = deliverySupplyForm()
    if request.method == 'POST':
        form = deliverySupplyForm(request.POST)
        itemname = request.POST.get('delivery_supply_itemname')
        description = request.POST.get('delivery_supply_description')
        unit = request.POST.get('delivery_supply_unit')
        quantity = request.POST.get('delivery_supply_quantity')

        if supplymainstorage.objects.filter(ItemName = itemname).exists() == False:
            if int(quantity) > 0:
                if form.is_valid():
                    form.save()
                    storageupdate = supplymainstorage()
                    storageupdate.ItemName = itemname
                    storageupdate.Description = description
                    storageupdate.Unit = unit
                    storageupdate.Remaining = 0
                    storageupdate.Quantity = quantity
                    storageupdate.save()
                    mapping = storagemapping()
                    mapping.Category = "Supply"
                    mapping.ItemName = itemname
                    mapping.CabinetNo = 0
                    mapping.Location = 0
                    mapping.ShelfNo = 0
                    mapping.LayerNo = 0
                    mapping.save()
                    messages.success(request, 'Record created for ' + itemname)
                    return redirect('inventorysystem-suppliesDeliver')
            else:
                    messages.info(request, "invalid quantity")
                    return redirect('inventorysystem-suppliesDeliver')

        elif supplymainstorage.objects.filter(ItemName = itemname).exists() == True:
            messages.info(request, 'Itemname: '  + itemname + ' already exist ')
            return redirect('inventorysystem-suppliesDeliver')        
    
    context = {
        'form': form,
        'info': info,
        'info1': info1,
    }

    return render(request, 'task/supplies-delivery.html', context)

def updateSuppliesDeliver(request, pk):
    data = supplymainstorage.objects.get(supplymainstorage_id=pk)
    form = updateDeliverySupplyForm(request.POST or None, instance=data)
    if request.method == 'POST':
        if int(request.POST.get('Remaining')) > 0:
            itemname = request.POST.get('ItemName')
            update_record = deliverysupply()
            update_record.delivery_supply_itemname = request.POST.get('ItemName')
            update_record.delivery_supply_unit = request.POST.get('Unit')
            update_record.delivery_supply_description = request.POST.get('Description')
            getdata = supplymainstorage.objects.get(ItemName = itemname)
            adding = int(getdata.Quantity) + int(request.POST.get('Remaining'))
            update_record.delivery_supply_remaining = adding
            update_record.delivery_supply_quantity = request.POST.get('Remaining')
            update_record.save()

            update_delivery = supplymainstorage()
            update_delivery.supplymainstorage_id = supplymainstorage.objects.get(ItemName = itemname).supplymainstorage_id
            update_delivery.ItemName = request.POST.get('ItemName')
            update_delivery.Unit = request.POST.get('Unit')
            update_delivery.Description = request.POST.get('Description')
            getdata = supplymainstorage.objects.get(ItemName = itemname)
            adding = int(getdata.Quantity) + int(request.POST.get('Remaining'))
            update_delivery.Remaining = 0
            update_delivery.Quantity = adding
            supplymainstorage.objects.filter(ItemName = itemname).delete()
            update_delivery.save()


            messages.success(request, 'Record updated for: ' + itemname)
            return redirect('inventorysystem-suppliesDeliver')
        else:
            messages.info(request, "invalid quantity")

    context = {
        'data': data,
        'form': form,
    }

    return render(request, 'task/update-supply-delivery.html', context)

def addItem(request):
    return render(request, 'task/add-new-item.html')

def equipmentDeliver(request):
    info = deliveryequipment.objects.all()
    info1 = equipmentmainstorage.objects.all()
    form = deliveryEquipmentForm()
    if request.method == 'POST':
        form = deliveryEquipmentForm(request.POST)
        itemname = request.POST.get('delivery_equipment_itemname')
        description = request.POST.get('delivery_equipment_description')
        unit = request.POST.get('delivery_equipment_unit')
        quantity = request.POST.get('delivery_equipment_quantity')

        if equipmentmainstorage.objects.filter(ItemName = itemname).exists() == False:
            if form.is_valid():
                form.save()
                storageupdate = equipmentmainstorage()
                storageupdate.ItemName = itemname
                storageupdate.Description = description
                storageupdate.Unit = unit
                storageupdate.Remaining = quantity
                storageupdate.save()
                mapping = storagemapping()
                mapping.Category = "Equipment"
                mapping.ItemName = itemname
                mapping.CabinetNo = 0
                mapping.Location = 0
                mapping.ShelfNo = 0
                mapping.LayerNo = 0
                mapping.save()
                messages.success(request, 'Record created for ' + itemname)
                return redirect('inventorysystem-equipmentDeliver')

        elif equipmentmainstorage.objects.filter(ItemName = itemname).exists() == True:
            getdata = equipmentmainstorage.objects.get(ItemName = itemname)
            updating = int(getdata.Remaining) + int(quantity)
            storageupdate = equipmentmainstorage()
            storageupdate.ItemName = itemname
            storageupdate.Description = description
            storageupdate.Unit = unit
            storageupdate.Remaining = updating
            equipmentmainstorage.objects.filter(ItemName = itemname).delete()
            storageupdate.save()
            form2 = deliveryequipment()
            form2.delivery_equipment_itemname = itemname
            form2.delivery_equipment_description = description
            form2.delivery_equipment_unit = unit
            form2.delivery_equipment_quantity = quantity
            form2.delivery_equipment_remaining = updating
            form2.save()
            messages.success(request, 'Record updated for ' + itemname)
            return redirect('inventorysystem-equipmentDeliver')        
    
    context = {
        'form': form,
        'info': info,
        'info1': info1,
    }
    return render(request, 'task/equipment-delivery.html', context)

#def addEquipment(request):
    return render(request, 'task/add-equipment.html')

def suppliesWithdraw(request):
    info = acceptSupplyRequests.objects.all()
    context = {
        'info': info,
    }
    return render(request, 'task/supplies-withdraw.html', context)

def suppliesWithdrawStatus(request, pk):
    data = acceptSupplyRequests.objects.get(id=pk)
    form = withdrawStatusForm(request.POST or None, instance=data)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('inventorysystem-suppliesWithdraw')

    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'task/supply-withdraw-update.html', context)

def equipmentWithdraw(request):
    info = requestequipment.objects.all()
    context = {
        'info': info,
    }
    return render(request, 'task/equipment-withdraw.html', context)

def createqrequipmentWithdraw(request):
    return render(request, 'task/createqr-equipment-withdraw.html')

def viewRequestSupply(request):
    info = requestsupply.objects.all()
    status = request.POST.get('request_supply_status')
    #if request.method == 'POST':
        #accept = requestsupply.objects.get(id=1)
        #accept.delete()
        #messages.success(request, 'Record updated')
    context = {
        'info': info,
        'status': status,
    }
    return render(request, 'task/view-request-supplies.html', context)

def editRequestSupply(request, pk):
    data = requestsupply.objects.get(acceptSupplyRequests_id=pk)
    form = requestSupplyForm(request.POST or None, instance=data)
    form2 = acceptSupplyRequestsForm()
    if request.method == 'POST':
        department = request.POST.get('request_supply_department')
        itemname = request.POST.get('request_supply_itemname')
        description = request.POST.get('request_supply_description')
        unit = request.POST.get('request_supply_unit')
        quantity = request.POST.get('request_supply_quantity')
        remaining = request.POST.get('request_supply_remaining')
        status = request.POST.get('request_supply_status')
        if form.is_valid():
            #user = form.cleaned_data.get('request_supply_department')
            #messages.success(request, 'Request supply record was updated for ' + user)
            form.save()
            form2 = acceptSupplyRequests()
            form2.arequest_supply_department = department
            form2.arequest_supply_itemname = itemname
            form2.arequest_supply_description = description
            form2.arequest_supply_unit = unit
            form2.arequest_supply_quantity = quantity
            form2.arequest_supply_remaining = remaining
            form2.arequest_supply_status = status
            form2.save()
            requestsupply.objects.filter(acceptSupplyRequests=pk).delete()
            return redirect('inventorysystem-viewRequestSupply')
    context = {
        'data': data,
        'form': form,
        'form2': form2,
    }

    return render(request, 'task/edit-request-supplies.html', context)

def viewRequestEquipment(request):

    return render(request, 'task/view-request-equipment.html')

def depRequestSupply(request):
    info1 = limitrecords.objects.all().filter(limit_department = request.user)
    info = requestsupply.objects.all().filter(request_supply_department = request.user)
    if request.method == 'POST':
        requestID = request.POST.get('requestID')
        requestqty = request.POST.get('requestqty')
        if limitrecords.objects.filter(limit_id = requestID).exists() == True:
            getdata3 = limitrecords.objects.get(limit_id = requestID)
            requesting = requestsupply()
            requesting.request_supply_itemname = getdata3.limit_item_name
            requesting.request_supply_description = getdata3.limit_description
            requesting.request_supply_unit = getdata3.limit_unit
            requesting.request_supply_quantity = requestqty
            requesting.request_supply_remaining = getdata3.limit_quantity
            requesting.request_supply_department = getdata3.limit_department
            requesting.request_supply_status = "pending"
            requesting.save()
            messages.success(request, 'Record created for ' + requestID)
    context = {
        'info1': info1,
        'info': info
    }
    return render(request, 'task/dep-request-supply.html', context)

def depRequestEquipment(request):
    info1 = limitrecords.objects.raw('SELECT limit_id from limitrecords WHERE limit_department = "OSA"')
    info = requestequipment.objects.all()

    context = {
        'info1': info1,
        'info': info
    }
    return render(request, 'task/dep-request-equipment.html', context)

def statusLimit(request):
    info = supplymainstorage.objects.all()
    info1 = limitrecords.objects.all()
    if request.method == 'POST':   
            itemname = request.POST.get('non-existing_itemname')
            description = request.POST.get('non-existing_description')
            unit = request.POST.get('non-existing_unit')
            quantity = request.POST.get('non-existing_quantity')
            department = request.POST.get('non-existing_department')
            
            limit = limitrecords()
            limit.limit_item_name = itemname
            limit.limit_description = description
            limit.limit_unit = unit
            limit.limit_quantity = quantity
            limit.limit_department = department
            limit.save()
            messages.success(request, 'Record created for ' + itemname)

    context = {
        'info': info,
        'info1': info1,
    }
    return render(request, 'task/status-limit.html', context)

def equipmentReturn(request):
    return render(request, 'task/equipment-return.html')

def storageMapping(request):
    info = storagemapping.objects.all()

    context = {
        'info': info
    }

    return render(request, 'task/storage-mapping.html', context)

def updateStoragemapping(request, pk):
    data = storagemapping.objects.get(storagemapping_id=pk)
    form = storageForm(request.POST or None, instance=data)
    if request.method == 'POST':
        if form.is_valid():
            #user = form.cleaned_data.get('request_supply_department')
            #messages.success(request, 'Request supply record was updated for ' + user)
            form.save()
            return redirect('inventorysystem-storageMapping')
    context = {
        'data': data,
        'form': form,
    }

    return render(request, 'task/update-storagemapping.html', context)

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
    supplydelivery = ['Itemname', 'Description', 'Unit',
                'Quantity', 'Remaining Quantity', 'Date']

    for col_num in range(len(supplydelivery)):
        ws.write(row_num,col_num, supplydelivery[col_num], supply_font)

    font_style = xlwt.XFStyle()

    rows = deliverysupply.objects.all().values_list(
        'delivery_supply_itemname', 'delivery_supply_description', 'delivery_supply_unit',
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
